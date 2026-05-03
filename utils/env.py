from __future__ import annotations

import os


def get_env_str(name: str, *, default: str) -> str:
    value = os.getenv(name)
    return value if value else default


def require_env_str(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def get_env_float(name: str, *, default: float) -> float:
    raw = os.getenv(name)
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError as exc:
        raise RuntimeError(f"Invalid float for {name}: {raw!r}") from exc

