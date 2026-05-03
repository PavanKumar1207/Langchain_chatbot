from __future__ import annotations

import os
from typing import Any, Optional


def _streamlit_secrets() -> Optional[dict[str, Any]]:
    try:
        import streamlit as st  # type: ignore
    except Exception:  # noqa: BLE001
        return None

    try:
        secrets = st.secrets
    except Exception:  # noqa: BLE001
        return None

    if secrets is None:
        return None
    return secrets  # type: ignore[return-value]


def get_secret_str(name: str, *, default: str) -> str:
    secrets = _streamlit_secrets()
    if secrets is not None:
        value = secrets.get(name)
        if value:
            return str(value)
    value = os.getenv(name)
    return value if value else default


def require_secret_str(name: str) -> str:
    secrets = _streamlit_secrets()
    if secrets is not None:
        value = secrets.get(name)
        if value:
            return str(value)
    value = os.getenv(name)
    if not value:
        raise RuntimeError(
            f"Missing required secret: {name}. Set it in Streamlit secrets (preferred) "
            f"or as an environment variable."
        )
    return value

