# Modular AI Chatbot (Streamlit + LangChain + Groq)

## Setup

1) Install dependencies:

```bash
pip install -r requirements.txt
```

2) Set environment variables:

- `GROQ_API_KEY` (required)
- `GROQ_MODEL` (optional override; default comes from `config/config.yaml`)
- `TEMPERATURE` (optional override; default comes from `config/config.yaml`)

Tip: copy `.env.example` to `.env` for local development.

3) Run:

```bash
streamlit run app.py
```

## Architecture

- `app.py` — Streamlit UI (thin)
- `config/config.yaml` — model + modes configuration
- `llm/` — Groq Chat model factory
- `prompts/` — system prompts per assistant mode
- `memory/` — per-session chat history stored in `st.session_state`
- `chains/` — `RunnableWithMessageHistory` wiring (Prompt + LLM + History)
- `utils/` — config + env loading helpers
