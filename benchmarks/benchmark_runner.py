import time


def run_benchmark(data):

    results = {}

    # Insert benchmark
    start = time.time()

    database = []

    for record in data:
        database.append(record)

    insert_time = time.time() - start

    results["insert_operation"] = {
        "records_inserted": len(database),
        "time_seconds": round(insert_time, 6)
    }


    # Read benchmark
    start = time.time()

    records = database.copy()

    read_time = time.time() - start

    results["read_operation"] = {
        "records_read": len(records),
        "time_seconds": round(read_time, 6)
    }


    # Query benchmark
    start = time.time()

    query_result = [
        record for record in database
        if "name" in record
    ]

    query_time = time.time() - start

    results["query_operation"] = {
        "matches_found": len(query_result),
        "time_seconds": round(query_time, 6)
    }


    # Update benchmark
    start = time.time()

    for record in database:
        record["benchmark"] = True

    update_time = time.time() - start

    results["update_operation"] = {
        "records_updated": len(database),
        "time_seconds": round(update_time, 6)
    }


    return results