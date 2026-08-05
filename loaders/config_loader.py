import yaml
import os


DEFAULT_CONFIG = {
    "benchmark": {
        "dataset": "dataset/sample_data.json",
        "operations": [
            "insert",
            "read",
            "query",
            "update"
        ]
    }
}


def load_config(config_path="config/config.yaml"):
    """
    Loads the YAML configuration file.
    If it does not exist or is empty,
    the default configuration is returned.
    """

    if not os.path.exists(config_path):
        return DEFAULT_CONFIG

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if config is None:
        return DEFAULT_CONFIG

    return config