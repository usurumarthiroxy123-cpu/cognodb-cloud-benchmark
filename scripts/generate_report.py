import json
import csv
import os
import matplotlib.pyplot as plt


JSON_RESULT_FILE = "results/benchmark_results.json"
CSV_RESULT_FILE = "results/benchmark_results.csv"
CHART_FILE = "results/benchmark_chart.png"


def load_results():
    if not os.path.exists(JSON_RESULT_FILE):
        raise FileNotFoundError(
            f"{JSON_RESULT_FILE} not found."
        )

    with open(JSON_RESULT_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def generate_csv(results):
    with open(
        CSV_RESULT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow([
            "Operation",
            "Metric",
            "Value"
        ])

        for operation, metrics in results.items():
            for metric, value in metrics.items():
                writer.writerow([
                    operation,
                    metric,
                    value
                ])


def generate_chart(results):

    operations = []
    execution_times = []

    for operation, metrics in results.items():

        operations.append(operation)

        execution_times.append(
            metrics.get("time_seconds", 0)
        )

    plt.figure(figsize=(8, 5))

    plt.bar(
        operations,
        execution_times
    )

    plt.title("CognODB Benchmark")

    plt.xlabel("Operations")

    plt.ylabel("Execution Time (Seconds)")

    plt.tight_layout()

    plt.savefig(CHART_FILE)

    plt.close()


def main():

    os.makedirs("results", exist_ok=True)

    results = load_results()

    generate_csv(results)

    generate_chart(results)

    print("CSV Report Generated")

    print("Chart Generated")


if __name__ == "__main__":
    main()