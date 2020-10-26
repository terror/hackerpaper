import requests
from urls import static_data, live_data


class Request:
    def __init__(self, id, type):
        self.id = id
        self.type = type

    def verify_params(self):
        return self.id or self.type

    def fetch_data(self):
        if not self.verify_params():
            return "Invalid parameters"

        try:
            if self.id and self.type:
                data = requests.get(static_data(self.id, self.type)).json()
            else:
                data = self.ids_to_json(requests.get(live_data(self.type)).json())
        except Exception as err:
            return "Error: {}".format(err)

        return data

    def ids_to_json(self, data):
        return [requests.get(static_data(i, "item")).json() for i in data]