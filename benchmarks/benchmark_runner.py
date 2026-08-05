import time
import json
import os


def run_benchmark(data):
    start_time = time.time()

    # Simulated graph operations
    total_records = len(data)

    # Simulate read operation
    read_start = time.time()
    records_read = [item for item in data]
    read_time = time.time() - read_start

    # Simulate query operation
    query_start = time.time()
    result = [item for item in data if "name" in item]
    query_time = time.time() - query_start

    end_time = time.time()

    results = {
        "total_records": total_records,
        "records_read": len(records_read),
        "query_results": len(result),
        "read_time_seconds": round(read_time, 6),
        "query_time_seconds": round(query_time, 6),
        "total_execution_time_seconds": round(end_time - start_time, 6)
    }

    return results