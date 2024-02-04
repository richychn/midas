class Agent:

    def __init__(self):

        self.name = ''
        self.language_model = ''
        self.embedding_model = ''

    def __repr__(self):
        return f"""
    Agent(
        name={self.name},
        language_model={self.language_model},
        embedding_model={self.embedding_model}
    )"""

    def load(self, f_agent):

        self.name = f_agent.get('name', '')
        self.language_model = f_agent.get('language_model', '')
        self.embedding_model = f_agent.get('embedding_model', '')

    def export_structure(self):
        return {
            "name": self.name,
            "language_model": self.language_model,
            "embedding_model": self.embedding_model
        }

class Prompt:

    def __init__(self):
        self.raw = ''
        self.mod = ''

    def __repr__(self):
        return f"""
    Prompt(
        raw={self.raw},
        mod={self.mod},
    )"""

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
        subquery_names = [name for name in self.data]
        return f"""
    SubQueryStruct(
        {',\n\t'.join(subquery_names)}
    )"""

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
        return f"SubQuery{self.name}"

    def load(self, name, struct):
        self.name = name
        self.string = struct.get('string', '')
        self.embedding = struct.get('embedding', '')

class CriteriaStruct:

    def __init__(self):
        self.data = {
            'UserCriteria': {},
            'AgentCriteria': {}
        }

    def __repr__(self):
        user_criteria_names = [name for name in self.data['UserCriteria']]
        agent_criteria_names = [name for name in self.data['AgentCriteria']]
        return f"""
    CriteriaStruct(
        UserCriteria(
            {',\n\t'.join(user_criteria_names)}
        )
        AgentCriteria(
            {',\n\t'.join(agent_criteria_names)}
        )
    )"""

    def load(self, f_criteria):

        for name, struct in f_criteria['user_criteria'].items():
            criteria = Criteria()
            criteria.load(name, struct)
            self.data['UserCriteria'][name] = criteria
        for name, struct in f_criteria['agent_criteria'].items():
            criteria = Criteria()
            criteria.load(name, struct)
            self.data['AgentCriteria'][name] = criteria

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
        return f"Criteria({self.name})"

    def load(self, name, f_criteria):
        self.name = name
        self.raw = f_criteria.get('raw', None)
        self.mod = f_criteria.get('mod', '')
