from typing import Dict, Any

import yaml


def load_config() -> Dict[str, Any]:
    _config_path = r"./config/browser.yaml"
    _config = yaml.safe_load(open(_config_path, "r"))

    return _config
