import json
import os


def load_dataset(dataset_path):
    """
    Load a JSON dataset and return it as a Python list.

    Parameters:
        dataset_path (str): Path to the JSON dataset file.

    Returns:
        list: Dataset records.

    Raises:
        FileNotFoundError: If the dataset file does not exist.
        ValueError: If the JSON file is empty or invalid.
    """

    if not os.path.exists(dataset_path):
        raise FileNotFoundError(
            f"Dataset not found: {dataset_path}"
        )

    with open(dataset_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON dataset.")

    if not isinstance(data, list):
        raise ValueError("Dataset must be a JSON array.")

    return data