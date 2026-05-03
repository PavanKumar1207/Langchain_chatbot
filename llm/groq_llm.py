from __future__ import annotations

from langchain_groq import ChatGroq

from utils.settings import AppSettings


def build_groq_chat_model(settings: AppSettings) -> ChatGroq:
    return ChatGroq(
        api_key=settings.groq_api_key,
        model=settings.groq_model,
        temperature=settings.temperature,
    )
