import json
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


def run_benchmark(graph, nodes):

    results = {}


    # Traversal benchmarks

    results["1_hop"] = measure_query(
        one_hop,
        graph,
        "user_1"
    )


    results["2_hop"] = measure_query(
        two_hop,
        graph,
        "user_1"
    )


    results["3_hop"] = measure_query(
        three_hop,
        graph,
        "user_1"
    )


    # Lookup benchmarks

    results["point_lookup"] = measure_lookup(
        point_lookup,
        nodes,
        "user_1"
    )


    results["filtered_lookup"] = measure_lookup(
        filtered_lookup,
        nodes,
        "type",
        "person"
    )


    # Aggregation

    results["aggregation"] = measure_aggregation(
        count_by_property,
        nodes,
        "type"
    )


    # Mixed workload

    results["mixed_workload"] = run_mixed_workload(
        graph
    )


    return results