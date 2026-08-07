import json
import yaml

from dotenv import load_dotenv

load_dotenv()

from adapters.adapter_factory import get_database_adapter

from benchmarks.benchmark_runner import run_benchmark

from loaders.graph_loader import (
    load_nodes,
    load_relationships
)


def load_config():

    with open(
        "config/config.yaml",
        "r"
    ) as file:

        return yaml.safe_load(file)


if __name__ == "__main__":


    print(
        "\n========== CognODB Cloud Benchmark ==========\n"
    )


    config = load_config()


    database_name = config["database"]["active"]


    print(
        f"Active database: {database_name}"
    )


    database = get_database_adapter(
        database_name
    )


    print(
        "\nLoading dataset..."
    )


    nodes = load_nodes(
        config["dataset"]["nodes"]
    )


    graph = load_relationships(
        config["dataset"]["relationships"]
    )


    print(
        f"Nodes loaded: {len(nodes)}"
    )


    relationships = sum(
        len(value)
        for value in graph.values()
    )


    print(
        f"Relationships loaded: {relationships}"
    )


    print(
        "\nRunning benchmarks...\n"
    )


    results = run_benchmark(
    database,
    graph,
    nodes
)


    # Store database name in result file
    results["database"] = database_name


    # Save separate result file for each database
    output_file = f"results/{database_name}_results.json"


    with open(
        output_file,
        "w"
    ) as file:

        json.dump(
            results,
            file,
            indent=4
        )


    print(
        f"Results saved to {output_file}"
    )
    database.close()