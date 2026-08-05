from adapters.database_adapter import DatabaseAdapter


class MemoryDatabase(DatabaseAdapter):
    """
    Simple in-memory database implementation used for benchmarking.
    """

    def __init__(self):
        self.records = []

    def insert(self, records):
        self.records.extend(records)
        return len(records)

    def read(self):
        return self.records.copy()

    def query(self):
        """
        Example query:
        Return all records that contain a 'name' field.
        """
        return [
            record
            for record in self.records
            if "name" in record
        ]

    def update(self):
        """
        Simulate updating every record.
        """
        count = 0

        for record in self.records:
            record["benchmark_updated"] = True
            count += 1

        return count