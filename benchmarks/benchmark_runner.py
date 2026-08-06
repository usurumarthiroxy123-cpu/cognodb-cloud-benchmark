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
WARMUP_RUNS = 2
BENCHMARK_RUNS = 10


def execute_warmup(function, *args):
    """
    Run warm-up executions before measurement.
    """
    for _ in range(WARMUP_RUNS):
        function(*args)



def flatten_relationships(graph):
    """
    Convert graph dictionary into relationship records
    for database loading.
    """

    relationships = []

    for source, targets in graph.items():

        for target in targets:

            relationships.append(
                {
                    "source": source,
                    "target": target
                }
            )

    return relationships



def run_benchmark(database, graph, nodes):
    database.clear_database()

    results = {
        "benchmark_config": {
            "warmup_runs": WARMUP_RUNS,
            "benchmark_runs": BENCHMARK_RUNS
        }
    }


    print("Loading data into database...")

    database.load_nodes(nodes)

    database.load_relationships(
        flatten_relationships(graph)
    )


    print("Database loading completed")


    # -------------------------
    # Traversal Benchmarks
    # -------------------------

    execute_warmup(
        one_hop,
        database,
        "user_1"
    )

    results["1_hop"] = measure_query(
        one_hop,
        database,
        "user_1",
        iterations=BENCHMARK_RUNS
    )


    execute_warmup(
        two_hop,
        database,
        "user_1"
    )

    results["2_hop"] = measure_query(
        two_hop,
        database,
        "user_1",
        iterations=BENCHMARK_RUNS
    )


    execute_warmup(
        three_hop,
        database,
        "user_1"
    )

    results["3_hop"] = measure_query(
        three_hop,
        database,
        "user_1",
        iterations=BENCHMARK_RUNS
    )



    # -------------------------
    # Lookup Benchmarks
    # -------------------------

    execute_warmup(
        point_lookup,
        database,
        "user_1"
    )

    results["point_lookup"] = measure_lookup(
        point_lookup,
        database,
        "user_1",
        iterations=BENCHMARK_RUNS
    )



    execute_warmup(
        filtered_lookup,
        database,
        "type",
        "person"
    )

    results["filtered_lookup"] = measure_lookup(
        filtered_lookup,
        database,
        "type",
        "person",
        iterations=BENCHMARK_RUNS
    )



    # -------------------------
    # Aggregation Benchmark
    # -------------------------

    execute_warmup(
        count_by_property,
        database,
        "type"
    )


    results["aggregation"] = measure_aggregation(
        count_by_property,
        database,
        "type",
        iterations=BENCHMARK_RUNS
    )



    # -------------------------
    # Mixed Workload
    # -------------------------

    results["mixed_workload"] = run_mixed_workload(
        database
    )


    return results