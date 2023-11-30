from tinydb import TinyDB, Query


class BatchEnvHandler:
    def __init__(self):
        self.db = TinyDB("configuration_db.json")

    def get_params(self, task_name):
        tasks = Query()
        docs = self.db.search(tasks.name == task_name)
        doc_type = type(docs)
        first = docs[0]
        return first["parameters"]
