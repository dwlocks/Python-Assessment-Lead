import os

from assignment import WidgetTask, GadgetTask
from env_handlers.local_env_handler import LocalEnvHandler
from task import Task


class TaskRunner:
    def __init__(self):
        self.env = os.getenv("TASK_ENV", None)
        # if self.env is None:
        #     raise MissingTaskEnvironmentError()
        if self.env == "local":
            self.env_handler = LocalEnvHandler()
        elif self.env == "batch":
            pass
        elif self.env == "lambda":
            pass
        else:
            # raise UnknownEnvironmentError()
            pass

    def run(self, task: Task):
        if isinstance(task, WidgetTask):
            parameters = self.env_handler.get_params("Widget")
        elif isinstance(task, GadgetTask):
            parameters = self.env_handler.get_params("Gadget")

        return task.run(parameters)
