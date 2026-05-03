# Langchain AI Chatbot (Streamlit + LangChain + Groq)

## Setup

1) Install dependencies:

```bash
pip install -r requirements.txt
```

2) Set Streamlit secrets:

Create `.streamlit/secrets.toml` (you can copy `.streamlit/secrets.toml.example`):

```toml
GROQ_API_KEY = "your_key_here"
```

Optional environment variable overrides:

- `GROQ_MODEL` (override; default comes from `config/config.yaml`)
- `TEMPERATURE` (override; default comes from `config/config.yaml`)

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
