# AGENTS.md

## 🤖 Project Context

This is a modular AI chatbot built using

 Python
 Streamlit (UI)
 LangChain (LLM orchestration)

The system follows a modular architecture with separate layers for LLM, memory, prompts, and chains.

---

## 📁 Project Structure

 `app.py` → Main Streamlit UI
 `config` → Environment variables and settings
 `llm` → LLM provider (OpenAI, etc.)
 `memory` → Conversation memory logic
 `prompts` → System prompt templates
 `chains` → LangChain conversation chain
 `utils` → Helper functions

Agents should respect this modular structure and avoid mixing concerns.

---

## ⚙️ Setup Commands

Install dependencies

```
pip install -r requirements.txt
```

Run the app

```
streamlit run app.py
```

---

## 🧠 LLM Rules

 Use LangChain for all LLM interactions (do NOT call APIs directly in UI)
 Default model `gpt-4o-mini`
 Temperature 0.7
 API keys must be loaded from environment variables only

---

## 🧠 Memory Rules

 Use `ConversationBufferMemory` for chat history
 Do NOT manually store messages outside memory module
 Memory must persist using `st.session_state`

---

## 📝 Prompt Rules

 Do NOT hardcode prompts inside business logic
 Always use `promptsprompt_templates.py`
 Support dynamic assistant roles

   General
   Tutor
   Coder

---

## 🔗 Chain Rules

 Use LangChain `ConversationChain`
 Chain must connect

   LLM
   Memory
 Do NOT bypass chain for direct LLM calls

---

## 🎨 UI Rules (Streamlit)

 UI must remain a thin layer
 No business logic inside `app.py`
 Only handle

   Inputoutput
   Session state
   Display

---

## 🧪 Code Style Guidelines

 Use Python 3.10+
 Write clean, modular functions
 Use meaningful variable names
 Keep functions small and reusable
 Add comments only where necessary

---

## 🚫 Strict Constraints

 ❌ Do NOT hardcode API keys
 ❌ Do NOT mix UI and backend logic
 ❌ Do NOT duplicate logic across modules
 ❌ Do NOT modify project structure without reason

---

## 🛠️ When Making Changes

 Always update the correct module (not app.py unless UI-related)
 Return full updated code when editing files
 Ensure compatibility with existing modules
 Keep changes minimal and modular

---

## 🚀 Future Extensions (Follow This Direction)

Agents may extend the project using

 RAG (Retrieval-Augmented Generation)
 Vector DB (FAISS  Chroma)
 LangChain Agents (tool usage)
 Multi-LLM support

---

## 🎯 Goal for AI Agent

Generate clean, modular, scalable code that follows

 Separation of concerns
 LangChain best practices
 Maintainability and extensibility

---
