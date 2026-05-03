from __future__ import annotations

import streamlit as st


def ensure_session_defaults() -> None:
    st.session_state.setdefault("assistant_mode", "General")
    st.session_state.setdefault("chat_history", None)
    st.session_state.setdefault("runnable", None)
    st.session_state.setdefault("runnable_mode", None)
