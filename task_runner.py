import json
import os

from assignment import WidgetTask, GadgetTask
from task import Task


class TaskRunner:
    def __init__(self):
        self.env = os.getenv("TASK_ENV", None)
        # if self.env is None:
        #     raise MissingTaskEnvironmentError()
        if self.env == "local":
            with open("parameters.json", "r") as param_f:
                self.all_parameters = json.load(param_f)
        elif self.env == "batch":
            pass
        elif self.env == "lambda":
            pass
        else:
            # raise UnknownEnvironmentError()
            pass

    def run(self, task: Task):
        if isinstance(task, WidgetTask):
            parameters = self.all_parameters["Widget"]
        elif isinstance(task, GadgetTask):
            parameters = self.all_parameters["Gadget"]

        return task.run(parameters)
