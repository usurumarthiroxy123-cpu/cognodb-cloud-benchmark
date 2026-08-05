from benchmarks.benchmark_runner import run_benchmark
from loaders.data_loader import load_dataset
import json
import os


def main():
    print("Starting CognODB Cloud Benchmark...")

    data = load_dataset()

    results = run_benchmark(data)

    print("\nBenchmark Results:")
    print(results)

    os.makedirs("results", exist_ok=True)

    with open("results/benchmark_results.json", "w") as file:
        json.dump(results, file, indent=4)

    print("\nResults saved to results/benchmark_results.json")


if __name__ == "__main__":
    main()