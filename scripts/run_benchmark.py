import argparse
import json
import os

from benchmarks.benchmark_runner import run_benchmark
from loaders.data_loader import load_dataset
from loaders.config_loader import load_config


def main():

    parser = argparse.ArgumentParser(
        description="CognODB Cloud Benchmark Runner"
    )

    parser.add_argument(
        "--dataset",
        default="dataset/sample_data.json",
        help="Path to dataset file"
    )

    parser.add_argument(
        "--output",
        default="results/benchmark_results.json",
        help="Output result file"
    )

    args = parser.parse_args()


    print("Starting CognODB Cloud Benchmark...")

    config = load_config()

    print("\nConfiguration:")
    print(config)


    data = load_dataset(args.dataset)


    results = run_benchmark(data)


    print("\nBenchmark Results:")
    print(results)


    os.makedirs(
        os.path.dirname(args.output),
        exist_ok=True
    )


    with open(args.output, "w") as file:
        json.dump(results, file, indent=4)


    print(
        f"\nResults saved to {args.output}"
    )


if __name__ == "__main__":
    main()