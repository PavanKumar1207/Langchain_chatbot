from __future__ import annotations

import streamlit as st

from chains.conversation import invoke_assistant
from memory.session_memory import clear_session_history, get_session_history
from utils.session import ensure_session_defaults
from utils.settings import AppSettings, load_settings


def main() -> None:
    st.set_page_config(page_title="Modular AI Chatbot", page_icon="💬", layout="centered")
    st.title("Modular AI Chatbot")

    ensure_session_defaults()

    try:
        settings: AppSettings = load_settings()
    except RuntimeError as exc:
        st.error(str(exc))
        st.info("Set `GROQ_API_KEY` in your environment (or a local `.env` file) and refresh.")
        return

    with st.sidebar:
        st.header("Settings")

        st.caption("Assistant mode")
        available_modes = list(settings.modes.keys())
        current_mode = st.session_state.get("assistant_mode", "General")
        if current_mode not in available_modes:
            current_mode = available_modes[0] if available_modes else "General"

        selected_mode = st.selectbox(
            label="Mode",
            options=available_modes,
            index=available_modes.index(current_mode) if available_modes else 0,
            label_visibility="collapsed",
        )
        st.session_state.assistant_mode = selected_mode

        st.caption("Model")
        st.write(f"`{settings.groq_model}`")

        st.caption("Temperature")
        st.write(f"`{settings.temperature}`")

        if st.button("Clear chat", type="secondary", use_container_width=True):
            clear_session_history()
            st.session_state.runnable = None
            st.session_state.runnable_mode = None
            st.rerun()

    history = get_session_history()
    for message in history.messages:
        role = "assistant"
        if getattr(message, "type", "") == "human":
            role = "user"
        with st.chat_message(role):
            st.markdown(message.content)

    user_text = st.chat_input("Type your message…")
    if not user_text:
        return

    with st.chat_message("user"):
        st.markdown(user_text)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            try:
                assistant_text = invoke_assistant(user_text)
            except Exception as exc:  # noqa: BLE001
                st.error(f"LLM error: {exc}")
                return
            st.markdown(assistant_text)


if __name__ == "__main__":
    main()
