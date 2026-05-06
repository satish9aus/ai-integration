# AI Integration — Personal Study Notes

> **Licensing notice**: The notebooks in this repository are personal study notes
> adapted from the following DeepLearning.AI courses:
>
> - *ChatGPT Prompt Engineering for Developers* — DeepLearning.AI & OpenAI (Andrew Ng, Isa Fulford)
> - *Building Systems with the ChatGPT API* — DeepLearning.AI & OpenAI (Andrew Ng, Isa Fulford)
>
> Course materials are the intellectual property of DeepLearning.AI. This repository
> is for **personal study only** and is not intended for redistribution. If you are
> looking for the original course content, enrol at [deeplearning.ai](https://www.deeplearning.ai).

---

## ChatGPT Prompt Engineering for Developers

| Notebook | Topic |
|---|---|
| `l1_prompting_guidelines.ipynb` | Clear instructions, delimiters, structured output, chain-of-thought |
| `l2_iterative_prompting.ipynb` | Iterative prompt development and refinement |
| `l3_summarizing.ipynb` | Summarizing with word/focus constraints; extract vs. summarize |
| `l4_inferring.ipynb` | Sentiment, emotion, entity extraction, zero-shot topic classification |
| `l5_transforming.ipynb` | Translation, tone, format conversion, spellcheck/grammar |
| `l6_expanding.ipynb` | Generating tailored responses; temperature parameter |
| `l7_chat_format.ipynb` | Chat roles (system/user/assistant), context, OrderBot |

## Building Systems with the ChatGPT API

| Notebook | Topic |
|---|---|
| `l1_language_models_chat_format_tokens.ipynb` | LLM training pipeline, tokenization, chat format, token counting |

---

## Setup

1. Copy `.env.example` to `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-...
   ```
2. Install dependencies:
   ```
   pip install openai python-dotenv tiktoken panel redlines
   ```
3. Run notebooks with Jupyter Lab or VS Code.
