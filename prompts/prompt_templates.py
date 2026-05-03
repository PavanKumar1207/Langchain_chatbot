from __future__ import annotations

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from utils.settings import AppSettings


def build_conversation_prompt(settings: AppSettings, mode: str) -> ChatPromptTemplate:
    system_text = settings.modes.get(mode) or settings.modes["General"]

    return ChatPromptTemplate.from_messages(
        [
            ("system", system_text),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ]
    )
