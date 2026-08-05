import unittest

from adapters.memory_database import MemoryDatabase
from benchmarks.benchmark_runner import run_benchmark


class TestBenchmark(unittest.TestCase):

    def setUp(self):

        self.database = MemoryDatabase()

        self.data = [
            {
                "id": 1,
                "name": "Alice"
            },
            {
                "id": 2,
                "name": "Bob"
            }
        ]

        self.operations = [
            "insert",
            "read",
            "query",
            "update"
        ]


    def test_insert_operation(self):

        result = run_benchmark(
            self.database,
            self.data,
            ["insert"]
        )

        self.assertIn(
            "insert",
            result
        )

        self.assertEqual(
            result["insert"]["records"],
            2
        )


    def test_read_operation(self):

        self.database.insert(self.data)

        result = run_benchmark(
            self.database,
            self.data,
            ["read"]
        )

        self.assertIn(
            "read",
            result
        )


    def test_query_operation(self):

        result = run_benchmark(
            self.database,
            self.data,
            ["insert", "query"]
        )

        self.assertEqual(
            result["query"]["matches"],
            2
        )


    def test_update_operation(self):

        result = run_benchmark(
            self.database,
            self.data,
            ["insert", "update"]
        )

        self.assertEqual(
            result["update"]["records_updated"],
            2
        )


if __name__ == "__main__":
    unittest.main()