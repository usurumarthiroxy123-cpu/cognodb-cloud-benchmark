import time


def run_benchmark(data):
    start = time.time()

    count = len(data)

    end = time.time()

    return {
        "records_processed": count,
        "execution_time_seconds": round(end - start, 6)
    }