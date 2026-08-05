class MemoryDatabase:

    def __init__(self):
        self.data = []


    def insert(self, records):
        self.data.extend(records)


    def read(self):
        return self.data.copy()


    def query(self):
        return [
            item for item in self.data
            if "name" in item
        ]


    def update(self):

        for item in self.data:
            item["updated"] = True

        return len(self.data)