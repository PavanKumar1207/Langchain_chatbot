from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from utils.config_loader import load_yaml_config
from utils.env import get_env_float, get_env_str
from utils.secrets import require_secret_str


@dataclass(frozen=True)
class AppSettings:
    groq_api_key: str
    groq_model: str
    temperature: float
    modes: Dict[str, str]


def load_settings() -> AppSettings:
    """
    Loads app settings from `config/config.yaml` and Streamlit secrets.

    Secrets (preferred):
      - GROQ_API_KEY (required)

    Environment variables (optional overrides / fallback):
      - GROQ_API_KEY (fallback)
      - GROQ_MODEL (override)
      - TEMPERATURE (override)
    """
    cfg = load_yaml_config()
    llm_cfg = cfg.get("llm") if isinstance(cfg.get("llm"), dict) else {}

    default_model = str(llm_cfg.get("model") or "llama-3.1-70b-versatile")
    default_temperature = float(llm_cfg.get("temperature") if llm_cfg.get("temperature") is not None else 0.7)

    modes_cfg = cfg.get("assistant_modes")
    if not isinstance(modes_cfg, dict) or not modes_cfg:
        raise RuntimeError("`assistant_modes` must be a non-empty mapping in config/config.yaml")
    modes: Dict[str, str] = {str(k): str(v) for k, v in modes_cfg.items()}

    groq_api_key = require_secret_str("GROQ_API_KEY")
    groq_model = get_env_str("GROQ_MODEL", default=default_model)
    temperature = get_env_float("TEMPERATURE", default=default_temperature)

    return AppSettings(
        groq_api_key=groq_api_key,
        groq_model=groq_model,
        temperature=temperature,
        modes=modes,
    )
