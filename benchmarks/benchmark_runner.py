import time

from workloads.traversal import (
    one_hop,
    two_hop,
    three_hop,
    measure_query
)

from workloads.lookup import (
    point_lookup,
    filtered_lookup,
    measure_lookup
)

from workloads.aggregation import (
    count_by_property,
    measure_aggregation
)

from workloads.mixed import (
    run_mixed_workload
)


# Benchmark configuration
WARMUP_RUNS = 10
BENCHMARK_RUNS = 100


def execute_warmup(function, *args):
    """
    Run warm-up executions before measurement.
    """
    for _ in range(WARMUP_RUNS):
        function(*args)



def run_benchmark(graph, nodes):

    results = {
        "benchmark_config": {
            "warmup_runs": WARMUP_RUNS,
            "benchmark_runs": BENCHMARK_RUNS
        }
    }


    # -------------------------
    # Traversal Benchmarks
    # -------------------------

    execute_warmup(one_hop, graph, "user_1")
    results["1_hop"] = measure_query(
        one_hop,
        graph,
        "user_1",
        iterations=BENCHMARK_RUNS
    )


    execute_warmup(two_hop, graph, "user_1")
    results["2_hop"] = measure_query(
        two_hop,
        graph,
        "user_1",
        iterations=BENCHMARK_RUNS
    )


    execute_warmup(three_hop, graph, "user_1")
    results["3_hop"] = measure_query(
        three_hop,
        graph,
        "user_1",
        iterations=BENCHMARK_RUNS
    )


    # -------------------------
    # Lookup Benchmarks
    # -------------------------

    execute_warmup(point_lookup, nodes, "user_1")
    results["point_lookup"] = measure_lookup(
        point_lookup,
        nodes,
        "user_1",
        iterations=BENCHMARK_RUNS
    )


    execute_warmup(filtered_lookup, nodes, "type", "person")
    results["filtered_lookup"] = measure_lookup(
        filtered_lookup,
        nodes,
        "type",
        "person",
        iterations=BENCHMARK_RUNS
    )


    # -------------------------
    # Aggregation Benchmark
    # -------------------------

    execute_warmup(count_by_property, nodes, "type")
    results["aggregation"] = measure_aggregation(
        count_by_property,
        nodes,
        "type",
        iterations=BENCHMARK_RUNS
    )


    # -------------------------
    # Mixed Workload
    # -------------------------

    # Mixed workload

    results["mixed_workload"] = run_mixed_workload(
    graph
    )


    return results