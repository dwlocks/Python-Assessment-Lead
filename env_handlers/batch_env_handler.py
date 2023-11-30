from tinydb import TinyDB, Query


class BatchEnvHandler:
    def __init__(self):
        print("-----------Loading db")
        self.db = TinyDB("configuration_db.json")

    def get_params(self, task_name):
        tasks = Query()
        docs = self.db.search(tasks.name == task_name)
        print(f"--------------{docs}")
        doc_type = type(docs)
        print(f"--------------{doc_type}")
        first = docs[0]
        return first["parameters"]
