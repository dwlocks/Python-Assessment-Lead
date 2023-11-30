class LambdaEnvHandler:
    def __init__(self, parameters):
        self.data = parameters

    def get_params(self, task_name=None):
        return self.data
