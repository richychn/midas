import json
import core


class Midas:

    def __init__(self):
        self.path = ''
        self.agent = core.Agent()
        self.prompt = core.Prompt()
        self.subquery = core.SubQueryStruct()
        self.criteria = core.CriteriaStruct()

    def __repr__(self):
        return f"Midas({self.agent}{self.prompt}{self.subquery}{self.criteria}"

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
            filepath=self.filepath

        agent_struct = self.export_structure()
                
        with open(filepath, "w") as outfile:
            json.dump(agent_struct, outfile, indent=4)