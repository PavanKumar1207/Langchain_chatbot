from __future__ import annotations

import streamlit as st
from langchain_core.chat_history import InMemoryChatMessageHistory


def get_session_history() -> InMemoryChatMessageHistory:
    """
    Returns per-session chat history stored in st.session_state.

    Uses the current LangChain chat history abstraction (no deprecated Memory classes).
    """
    history = st.session_state.get("chat_history")
    if isinstance(history, InMemoryChatMessageHistory):
        return history

    history = InMemoryChatMessageHistory()
    st.session_state.chat_history = history
    return history


def clear_session_history() -> None:
    st.session_state.chat_history = InMemoryChatMessageHistory()

