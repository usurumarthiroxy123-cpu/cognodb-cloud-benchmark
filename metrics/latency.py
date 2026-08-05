import time


def measure_latency(function, *args, iterations=100):
    """
    Executes a function multiple times
    and returns latency statistics.
    """

    latencies = []

    for _ in range(iterations):
        start = time.perf_counter()

        function(*args)

        end = time.perf_counter()

        latencies.append((end - start) * 1000)

    latencies.sort()

    p50_index = int(len(latencies) * 0.50)
    p95_index = int(len(latencies) * 0.95)

    return {
        "p50_ms": round(latencies[p50_index], 4),
        "p95_ms": round(latencies[p95_index], 4),
        "iterations": iterations
    }