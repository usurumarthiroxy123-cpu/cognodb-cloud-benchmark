import time


def measure_time(function):
    """
    Measures execution time of a function.
    """

    start = time.perf_counter()

    result = function()

    end = time.perf_counter()

    return result, round(end - start, 6)


def run_benchmark(database, data, operations):
    """
    Runs benchmark operations on a database adapter.

    Parameters:
        database: Database adapter instance
        data: Dataset records
        operations: List of operations to execute

    Returns:
        Dictionary containing benchmark results
    """

    results = {}

    if "insert" in operations:

        _, execution_time = measure_time(
            lambda: database.insert(data)
        )

        results["insert"] = {
            "records": len(data),
            "time_seconds": execution_time
        }


    if "read" in operations:

        records, execution_time = measure_time(
            database.read
        )

        results["read"] = {
            "records": len(records),
            "time_seconds": execution_time
        }


    if "query" in operations:

        records, execution_time = measure_time(
            database.query
        )

        results["query"] = {
            "matches": len(records),
            "time_seconds": execution_time
        }


    if "update" in operations:

        updated, execution_time = measure_time(
            database.update
        )

        results["update"] = {
            "records_updated": updated,
            "time_seconds": execution_time
        }


    return results