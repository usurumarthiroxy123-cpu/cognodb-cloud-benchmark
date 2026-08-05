from benchmarks.benchmark_runner import run_benchmark
from loaders.data_loader import load_dataset


def main():
    print("Starting CognODB Cloud Benchmark...")

    data = load_dataset()

    results = run_benchmark(data)

    print("\nBenchmark Results:")
    print(results)


if __name__ == "__main__":
    main()