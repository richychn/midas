import os
import json
import midas.core as c
import midas.prompts as p
import midas.embeddings as e

import openai
from openai import OpenAI
from dotenv import load_dotenv

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

        completion_dict = self.generate_subqueries()
        completion_dict = self.generate_subquery_embeddings(completion_dict)
        self.subquery.parse(completion_dict)

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
