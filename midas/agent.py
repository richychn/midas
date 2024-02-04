import os
import json
import midas.core as c
import midas.utils as u
import midas.query as q
import midas.prompts as p
import midas.embeddings as e

import openai

from itertools import repeat

from openai import OpenAI
from dotenv import load_dotenv
from concurrent.futures import ProcessPoolExecutor

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]


class Midas:

    def __init__(self):
        self.path = ''
        self.client = OpenAI()
        self.is_trained = False

        self.agent = c.Agent()
        self.prompt = c.Prompt()
        self.subquery = c.SubQueryStruct()
        self.criteria = c.CriteriaStruct()

    def __repr__(self):
        return f"Midas({self.agent}{self.prompt}{self.subquery}{self.criteria}\n)"

    def set_objective(self, objective):
        self.prompt.raw = objective
        self.prompt.mod = objective

        subquery_dict = self.generate_subqueries()
        subquery_dict = self.generate_subquery_embeddings(subquery_dict)
        criteria_dict = self.generate_criteria()
        
        self.subquery.parse(subquery_dict)
        self.criteria.parse(criteria_dict)

    def generate_subqueries(self):

        completion = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": p.SUBQUERY_CONTEXT},
                {"role": "user", "content": self.prompt.mod}
            ],
            temperature=0
        )

        completion_dict = json.loads(completion.choices[0].message.content)

        completion_dict = {name: {'string': string, 'embedding': []} for name, string in completion_dict.items()}

        return completion_dict

    def generate_subquery_embeddings(self, completion_dict):

        for name, struct in completion_dict.items():

            completion_dict[name]['embedding'] = e.embed_string(struct['string'])

        return completion_dict

    def generate_criteria(self):

        completion = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": p.CRITERIA_CONTEXT},
                {"role": "user", "content": self.prompt.mod}
            ],
            temperature=0
        )

        completion_dict = json.loads(completion.choices[0].message.content)

        return completion_dict

    def add_criteria(self, dict_lst):
        self.criteria.add_user_criteria(dict_lst)

    def generate_criteria_str(self):
        criteria_str = '\nOutput Criteria:\n'
        for name, struct in (self.criteria.data['UserCriteria'] | self.criteria.data['AgentCriteria']).items():
            criteria_str += f" - {name}: {struct.mod}\n"

        return criteria_str

    def run(self, convo_id, sort_key=None):

        chunk_str = self.generate_chunk_str(convo_id, sort_key)

        criteria_str = self.generate_criteria_str()

        completion = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": self.prompt.mod + criteria_str},
                {"role": "user", "content": chunk_str}
            ],
            temperature=0
        )

        output = completion.choices[0].message.content

        return output
    
    def evaluate(self, convo_id, sort_key=None):

        criteria_str = self.generate_criteria_str()

        output = self.run(convo_id, sort_key)

        eval_completion = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": p.EVAL_CONTEXT},
                {"role": "user", "content": 'Original User Prompt:\n' + self.prompt.mod + "="*30 + criteria_str + "="*30 + 'Model Output:\n' + output}
            ],
            temperature=0
        )

        eval = eval_completion.choices[0].message.content

        mod_completion = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": p.MOD_CONTEXT},
                {"role": "user", "content": "Feedback:\n" + eval + "="*30 + 'Original User Prompt:\n' + self.prompt.mod}
            ],
            temperature=0
        )

        mod = mod_completion.choices[0].message.content

        return output, eval, mod

    def load(self, filepath):

        self.path = filepath
        f = json.load(open(self.path,))

        self.agent.load(f['agent'])
        self.prompt.load(f['prompt'])
        self.subquery.load(f['subquery'])
        self.criteria.load(f['criteria'])

    def export_structure(self):
        export_structure = {
            "agent": self.agent.export_structure(),
            "prompt": self.prompt.export_structure(),
            "subquery": self.subquery.export_structure(),
            "criteria": self.criteria.export_structure()
        }
        return export_structure

    def save(self, filepath=None):

        if filepath is None:
            filepath = self.filepath

        agent_struct = self.export_structure()

        with open(filepath, "w") as outfile:
            json.dump(agent_struct, outfile, indent=4)

    def generate_chunk_str(self, convo_id, sort_key=None):
        
        def retrieve_subquery_chunks():
            with ProcessPoolExecutor() as executor:
                results = list(executor.map(
                    q.agent_subquery_retrieval,
                    self.subquery.data.items(),
                    repeat(convo_id)
                ))
            
            retrieved_chunks = dict(results)
        
            return retrieved_chunks
        
        def process_chunks(retrieved_chunks):
            processed_chunks = {}
            
            for subquery, textnode_list in retrieved_chunks.items():
                for textnode in textnode_list:
            
                    text = textnode.text
                    metadata_str = textnode.get_metadata_str()
                    metadata_lst = metadata_str.split(textnode.metadata_seperator)
                    metadata_dct = u.list_to_dict(metadata_lst)
            
                    if text not in processed_chunks:
                        processed_chunks[text] = {
                            'metadata': metadata_dct,
                            'topics': [subquery]
                        }
                    else:
                        processed_chunks[text]['topics'].append(subquery)
            
            processed_chunks_lst = u.dict_to_list(processed_chunks)
        
            return processed_chunks_lst
        
        def process_chunks_lst(processed_chunks_lst):
            retrieved_str = ''
            
            for chunk in processed_chunks_lst:
                chunk_str = '\n' + '=' * 50 + '\n'
                chunk_str += u.translate_to_string(chunk['metadata']) + '\n'
                chunk_str += f'topics: {chunk['topics']}' + '\n\n'
                chunk_str += chunk['text'] + '\n'
            
                retrieved_str += chunk_str
        
            return retrieved_str

        retrieved_chunks = retrieve_subquery_chunks()
        processed_chunks_lst = process_chunks(retrieved_chunks)

        if sort_key:
            processed_chunks_lst = sorted(processed_chunks_lst, key=sort_key)

        chunk_str = process_chunks_lst(processed_chunks_lst)

        return chunk_str
