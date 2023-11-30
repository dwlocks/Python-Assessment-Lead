import os

from assignment import WidgetTask, GadgetTask
from env_handlers.batch_env_handler import BatchEnvHandler
from env_handlers.lambda_env_handler import LambdaEnvHandler
from env_handlers.local_env_handler import LocalEnvHandler
from task import Task


class TaskRunner:
    def __init__(self, parameters=None):
        self.env = os.getenv("TASK_ENV", None)
        # if self.env is None:
        #     raise MissingTaskEnvironmentError()
        if self.env == "local":
            self.env_handler = LocalEnvHandler()
        elif self.env == "batch":
            self.env_handler = BatchEnvHandler()
        elif self.env == "lambda":
            self.env_handler = LambdaEnvHandler(parameters)
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
