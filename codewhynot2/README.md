# CodeWhyNot 2.0

A modular, pluggable, and scalable system for code generation, causal analysis, and counterfactual explanation using LLMs.

## Features
- Pluggable LLM backend (local, Hugging Face API, OpenAI, Replicate)
- Causal graph-based prompt intervention
- AST-based code diffing and fidelity scoring
- Streamlit UI for interactive exploration

## Quick Start
1. Copy `.env.example` to `.env` and fill in your API keys.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run src/ui/app.py`

See `docs/setup_guide.md` for full instructions.
