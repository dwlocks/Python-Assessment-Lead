import json


class LocalEnvHandler:
    def __init__(self):
        # TODO: Don't hardcode this here.
        with open("parameters.json", "r") as param_f:
            self.data = json.load(param_f)

    def get_params(self, task_name):
        return self.data[task_name]