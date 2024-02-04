import midas.utils as u


class Agent:

    def __init__(self, name):

        self.name = name

    def __repr__(self):

        repr_string = u.bold(f'Midas({self.name})\n')

        return repr_string

    def load(self, f_agent):

        self.name = f_agent.get('name', '')

    def export_structure(self):
        return {
            "name": self.name
        }


class Prompt:

    def __init__(self):
        self.raw = ''
        self.mod = ''

    def __repr__(self):

        repr_string = u.bold('Original User Prompt:\n')
        repr_string += self.raw + '\n'

        if self.raw != self.mod:
            repr_string += u.bold('Modified User Prompt:\n')
            repr_string += self.mod + '\n'

        return repr_string

    def load(self, f_prompt):
        self.raw = f_prompt.get('raw', '')
        self.mod = f_prompt.get('mod', '')

    def export_structure(self):
        return {
            "raw": self.raw,
            "mod": self.mod
        }

class SubQueryStruct:

    def __init__(self):
        self.data = {}

    def __repr__(self):

        repr_string = u.bold('Subqueries:\n')

        for name, subquery in self.data.items():
            repr_string += f"{subquery}"

        return repr_string

    def parse(self, completion_dict):
        for name, struct in completion_dict.items():
            if name not in self.data:
                self.data[name] = SubQuery()
            self.data[name].parse(name, struct['string'], struct['embedding'])

    def load(self, f_subquery):
        for name, struct in f_subquery.items():
            subquery = SubQuery()
            subquery.load(name, struct)
            self.data[name] = subquery

    def export_structure(self):
        export_structure = {name: {
            'string': struct.string,
            'embedding': struct.embedding
        } for name, struct in self.data.items()}
        return export_structure


class SubQuery:

    def __init__(self):
        self.name = ''
        self.string = ''
        self.embedding = ''

    def __repr__(self):
        return f" - [{self.name}] {self.string}\n"

    def load(self, name, struct):
        self.name = name
        if isinstance(struct, dict):
            self.string = struct.get('string', '')
            self.embedding = struct.get('embedding', '')
        else:
            self.string = struct.string
            self.embedding = struct.embedding

    def parse(self, name, string, embedding):
        self.name = name
        self.string = string
        self.embedding = embedding


class CriteriaStruct:

    def __init__(self):
        self.data = {
            'UserCriteria': {},
            'AgentCriteria': {}
        }

    def __repr__(self):

        repr_string = ''

        if self.data['AgentCriteria'].items():

            repr_string += u.bold('Agent Criteria:\n')

            for name, criteria in self.data['AgentCriteria'].items():
                repr_string += f"{criteria}\n"

        if self.data['UserCriteria'].items():

            if self.data['AgentCriteria'].items():
                repr_string += '\n'

            repr_string += u.bold('User Criteria:\n')

            for name, criteria in self.data['UserCriteria'].items():
                repr_string += f"{criteria}\n"

        return repr_string
 
    def add_user_criteria(self, dict_lst):

        for struct in dict_lst:
            for name, criteria in struct.items():
                c = Criteria()
                c.set(name, criteria)
                self.data['UserCriteria'][name] = c

    def parse(self, criteria_dict):

        for name, criteria in criteria_dict.items():
            c = Criteria()
            c.set(name, criteria)
            self.data['AgentCriteria'][name] = c

    def load(self, f_criteria):

        for name, struct in f_criteria['user_criteria'].items():
            c = Criteria()
            c.load(name, struct)
            self.data['UserCriteria'][name] = c

        for name, struct in f_criteria['agent_criteria'].items():
            c = Criteria()
            c.load(name, struct)
            self.data['AgentCriteria'][name] = c

    def export_structure(self):
        export_structure = {
            'user_criteria': {
                name: {
                    'raw': struct.raw,
                    'mod': struct.mod
                }
                for name, struct in self.data['UserCriteria'].items()
            },
            'agent_criteria': {
                name: {
                    'mod': struct.mod
                }
                for name, struct in self.data['AgentCriteria'].items()
            }
        }
        return export_structure


class Criteria:

    def __init__(self):
        self.name = ""
        self.type = ""
        self.raw = None
        self.mod = ""

    def __repr__(self):
        return f" - [{self.name}] {self.mod}"
    
    def set(self, name, criteria_str):
        self.name = name
        self.raw = criteria_str
        self.mod = criteria_str

    def load(self, name, f_criteria):
        self.name = name
        self.raw = f_criteria.get('raw', None)
        self.mod = f_criteria.get('mod', '')
