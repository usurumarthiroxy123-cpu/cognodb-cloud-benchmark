import logging
import os


def setup_logger():
    """
    Creates and returns a logger for the benchmark framework.
    Logs are stored in logs/benchmark.log
    """

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("CognODBBenchmark")

    # Prevent duplicate log handlers
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        "logs/benchmark.log",
        mode="a"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger