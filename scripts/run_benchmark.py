import argparse
import json
import os
import sys

from adapters.memory_database import MemoryDatabase
from benchmarks.benchmark_runner import run_benchmark
from loaders.config_loader import load_config
from loaders.data_loader import load_dataset
from scripts.logger import setup_logger


def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser(
        description="CognODB Cloud Benchmark Framework"
    )

    parser.add_argument(
        "--config",
        default="config/config.yaml",
        help="Configuration file path"
    )

    parser.add_argument(
        "--dataset",
        default=None,
        help="Override dataset path"
    )

    parser.add_argument(
        "--output",
        default="results/benchmark_results.json",
        help="Output JSON file"
    )

    args = parser.parse_args()

    try:
        logger.info("Loading configuration...")

        config = load_config(args.config)

        dataset_path = (
            args.dataset
            if args.dataset
            else config["benchmark"]["dataset"]
        )

        operations = config["benchmark"]["operations"]

        logger.info(f"Loading dataset: {dataset_path}")

        data = load_dataset(dataset_path)

        logger.info(f"Loaded {len(data)} records")

        database = MemoryDatabase()

        logger.info("Running benchmark...")

        results = run_benchmark(
            database,
            data,
            operations
        )

        os.makedirs(
            os.path.dirname(args.output),
            exist_ok=True
        )

        with open(
            args.output,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                results,
                file,
                indent=4
            )

        print("\n========== CognODB Cloud Benchmark ==========\n")

        for operation, metrics in results.items():
            print(f"{operation.upper()}")

            for key, value in metrics.items():
                print(f"  {key}: {value}")

            print()

        print(f"Results saved to: {args.output}")

        logger.info("Benchmark completed successfully.")

    except Exception as error:

        logger.exception(str(error))

        print("\nERROR:")
        print(error)

        sys.exit(1)


if __name__ == "__main__":
    main()