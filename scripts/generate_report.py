import json
import matplotlib.pyplot as plt


def generate_chart():

    with open("results/benchmark_results.json", "r") as file:
        results = json.load(file)

    operations = []
    times = []

    for operation, data in results.items():
        operations.append(operation)
        times.append(data["time_seconds"])

    plt.figure(figsize=(8, 5))

    plt.bar(operations, times)

    plt.xlabel("Operations")
    plt.ylabel("Execution Time (seconds)")
    plt.title("CognODB Benchmark Performance")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("results/benchmark_chart.png")

    print("Chart generated successfully!")


if __name__ == "__main__":
    generate_chart()