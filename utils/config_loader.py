from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import yaml


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_yaml_config() -> Dict[str, Any]:
    path = project_root() / "config/config.yaml"
    if not path.exists():
        raise RuntimeError(f"Missing config file: {path}")
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise RuntimeError(f"Invalid YAML in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise RuntimeError(f"Config root must be a mapping in {path}")
    return data

