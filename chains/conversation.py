from __future__ import annotations

import streamlit as st
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate

from llm.groq_llm import build_groq_chat_model
from memory.session_memory import get_session_history
from prompts.prompt_templates import build_conversation_prompt
from utils.settings import load_settings


def _build_base_runnable(prompt: ChatPromptTemplate):
    llm = build_groq_chat_model(load_settings())
    return prompt | llm


def get_conversation_runnable() -> RunnableWithMessageHistory:
    """
    Returns a per-session chat runnable stored in st.session_state.
    Recreated when the assistant mode changes.
    """
    settings = load_settings()
    mode = st.session_state.get("assistant_mode", "General")

    runnable = st.session_state.get("runnable")
    runnable_mode = st.session_state.get("runnable_mode")
    if isinstance(runnable, RunnableWithMessageHistory) and runnable_mode == mode:
        return runnable

    prompt = build_conversation_prompt(settings=settings, mode=mode)
    base = _build_base_runnable(prompt)

    runnable = RunnableWithMessageHistory(
        base,
        get_session_history=lambda session_id: get_session_history(),
        input_messages_key="input",
        history_messages_key="history",
        output_messages_key=None,
    )

    st.session_state.runnable = runnable
    st.session_state.runnable_mode = mode
    return runnable


def invoke_assistant(user_text: str) -> str:
    runnable = get_conversation_runnable()
    result = runnable.invoke(
        {"input": user_text},
        config={"configurable": {"session_id": "streamlit"}},
    )
    if isinstance(result, AIMessage):
        return result.content
    return str(result)
