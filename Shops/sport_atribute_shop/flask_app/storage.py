import json 


class Storage:

    def __init__(self, path):
        self.path = path

    def get(self, *args, **kwargs):
        with open (self.path, "r") as file:
            data = json.load(file)
        return data

    def get_by_email(self, email):
        data = self.get()
        result = list(filter(lambda acc: acc.get("email") == email, data))
        if not result:
            result = None
        else:
            result = result[0]
        return result

    def add(self, data):
        storage_data = self.get()
        storage_data.append(data)
        with open(self.path, "w") as file:
            json.dump(storage_data, file)
