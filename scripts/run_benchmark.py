import json

from benchmarks.benchmark_runner import run_benchmark

from metrics.load_metrics import measure_loading

from loaders.graph_loader import (
    load_nodes,
    load_relationships
)



if __name__ == "__main__":


    print(
        "\n========== CognODB Cloud Benchmark ==========\n"
    )


    print(
        "Loading dataset..."
    )


    node_load_result = measure_loading(
        load_nodes,
        "datasets/nodes.csv"
    )


    relationship_load_result = measure_loading(
    load_relationships,
    "datasets/relationships.csv",
    count_function=lambda graph: sum(
        len(value)
        for value in graph.values()
    )
)


    nodes = load_nodes(
        "datasets/nodes.csv"
    )


    graph = load_relationships(
        "datasets/relationships.csv"
    )


    relationships = sum(
        len(value)
        for value in graph.values()
    )


    print(
        f"Nodes loaded: {len(nodes)}"
    )


    print(
        f"Relationships loaded: {relationships}"
    )


    print("\nRunning benchmarks...\n")


    results = run_benchmark(
        graph,
        nodes
    )


    results["data_loading"] = {

        "nodes": node_load_result,

        "relationships": relationship_load_result

    }


    for name, result in results.items():

        print(
            name.upper()
        )

        print(
            result
        )

        print()



    with open(
        "results/benchmark_results.json",
        "w"
    ) as file:

        json.dump(
            results,
            file,
            indent=4
        )


    print(
        "Results saved to results/benchmark_results.json"
    )