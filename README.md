# AI Integration Engineer Learning Pathway

High-quality, practical study resources organized by stage so you can go from beginner to job-ready without getting overwhelmed.

> **Licensing notice**: The notebooks in this repository are personal study notes
> adapted from the following DeepLearning.AI courses:
>
> - *ChatGPT Prompt Engineering for Developers* - DeepLearning.AI & OpenAI (Andrew Ng, Isa Fulford)
> - *Building Systems with the ChatGPT API* - DeepLearning.AI & OpenAI (Andrew Ng, Isa Fulford)
>
> Course materials are the intellectual property of DeepLearning.AI. This repository
> is for personal study only and is not intended for redistribution. If you are
> looking for the original course content, enroll at [deeplearning.ai](https://www.deeplearning.ai).

---

## 1. Programming and API Foundations

### Python

Free:
- *CS50P (Harvard)*
- *Python for Everybody (Coursera)*

Hands-on:
- *Automate the Boring Stuff* (book + course)

### APIs and Backend Basics

- *Postman API Fundamentals* (free)
- *REST APIs with Flask/FastAPI* (freeCodeCamp)
- FastAPI docs: https://fastapi.tiangolo.com/

Focus:
- making requests
- building endpoints
- handling JSON

---

## 2. AI and LLM Fundamentals

### Intro to LLMs

- DeepLearning.AI - ChatGPT Prompt Engineering (Andrew Ng)
- DeepLearning.AI - Building Systems with ChatGPT API

### Practical Guides

- OpenAI API docs
- Anthropic docs

### YouTube (high-signal channels)

- Andrej Karpathy
- AssemblyAI
- Nicholas Renotte

Focus:
- prompt design
- tokens
- context windows
- basic API usage

---

## 3. AI Integration (Most Important)

### Frameworks

- LangChain docs
- LlamaIndex docs

Pick one first and go deep.

### Vector Databases

- Pinecone Learn
- Weaviate Academy

### RAG Learning

- "Build a RAG system" (DeepLearning.AI short course)
- "Chat with PDFs LangChain" walkthroughs
- "RAG from scratch Python" walkthroughs

Focus:
- embeddings
- chunking
- retrieval + generation pipeline

---

## 4. Backend and System Design

### Backend Engineering

- *FastAPI Full Course* (freeCodeCamp)
- *Backend Developer Roadmap* (roadmap.sh)

### System Design (lightweight)

- ByteByteGo (YouTube + blog)
- *Designing Data-Intensive Applications* (optional deep read)

Focus:
- async requests
- multi-user handling
- service boundaries

---

## 5. Deployment and DevOps

### Essentials

- Docker
- Deploy with Vercel/Render/Railway (easy path)
- AWS/GCP basics (later)

### CI/CD

- GitHub Actions (basic workflows)

---

## 6. Real Project Tutorials (Very Important)

Do not just watch. Build along.

- freeCodeCamp AI app builds
- "Build SaaS with AI" tutorials
- GitHub search: "AI RAG app FastAPI" -> clone + modify

---

## 7. Prompt Engineering (Advanced but Useful)

- OpenAI Cookbook
- Prompt Engineering Guide (promptingguide.ai)

---

## 8. Tools to Practice

- OpenAI / Anthropic APIs
- FastAPI
- LangChain or LlamaIndex
- Pinecone or FAISS
- PostgreSQL
- Redis (optional)

---

## Suggested Learning Stack (Keep It Simple)

1. Python
2. FastAPI
3. OpenAI API
4. LangChain
5. Pinecone
6. Docker

---

## How to Study Effectively

- 20% learning
- 80% building

For every topic:
- watch 1-2 tutorials
- build a small project immediately

---

## Detailed Roadmap: Beginner to Job-Ready

An AI Integration Engineer sits at the intersection of software engineering, APIs, and applied AI. This path is practical and system-focused, not theory-heavy like a traditional ML engineering track.

### 1) Foundations (2-4 weeks)

Core skills:
- Python (primary), optionally Node.js
- REST APIs (requests, auth, JSON)
- Git + GitHub
- basic Linux/terminal

Learn:
- HTTP methods, headers, status codes
- JSON parsing and transformation
- writing clean scripts and small services

Output goal:
- build a simple API client (weather app, stock tool, etc.)

### 2) AI Fundamentals (3-6 weeks)

Key concepts:
- LLMs (GPT, Claude, etc.)
- tokens, embeddings, context windows
- prompt engineering basics
- fine-tuning vs RAG

Learn tools:
- OpenAI / Anthropic APIs
- Hugging Face (basic usage)

Output goal:
- chatbot using API
- prompt experiments (summarizer, classifier)

### 3) AI Integration Skills (Core Stage) (4-8 weeks)

Learn how to:
- connect AI to real systems
- build pipelines with APIs, databases, and tools

Key topics:
- function calling/tool use
- RAG pipelines (embeddings + vector DBs)
- file ingestion (PDFs, docs)
- preprocessing

Frameworks:
- LangChain or LlamaIndex
- FastAPI (serving)

Output projects:
- chat with documents app
- knowledge base assistant (RAG)
- AI workflow pipeline (input -> process -> output)

### 4) Systems and Production (4-6 weeks)

Learn:
- backend architecture
- async processing
- caching (Redis)
- queues (Celery/RabbitMQ)
- logging and monitoring

AI-specific concerns:
- latency optimization
- token cost control
- prompt versioning
- robust error handling for LLM outputs

Output goal:
- deploy a production-style AI service with API endpoint + usage logs

### 5) Deployment and DevOps (2-4 weeks)

Learn:
- Docker
- cloud basics (AWS/GCP/Azure)
- CI/CD pipelines
- serverless vs containers

Output goal:
- deploy on cloud or Vercel/Railway/Render

### 6) Advanced Integration (Optional)

Go deeper into:
- multi-agent systems
- tool-using agents
- workflow automation (Zapier, Make, n8n)
- enterprise integrations (CRM/ERP)

Output ideas:
- Slack/email assistant
- automated business workflow agent

### 7) Portfolio (Critical)

Build 3-5 strong projects.

Must-have:
1. RAG chatbot (docs/knowledge base)
2. AI-powered API service
3. Workflow automation tool (AI + external APIs)

Bonus:
- Chrome extension with AI
- Slack/Teams bot
- SaaS-style mini product

### Realistic Timeline

- Fast-track (intense): 3-4 months
- Balanced: 5-6 months

### Common Mistakes to Avoid

- spending months on ML theory
- ignoring backend engineering
- building only toy chatbots
- not deploying projects

### What Clients and Teams Value

- ability to plug AI into real systems
- shipping working products
- API + data pipeline fluency
- workflow-oriented thinking

---

## Course Notebooks Reference

### ChatGPT Prompt Engineering for Developers

| Notebook | Topic |
|---|---|
| `l1_prompting_guidelines.ipynb` | Clear instructions, delimiters, structured output, chain-of-thought |
| `l2_iterative_prompting.ipynb` | Iterative prompt development and refinement |
| `l3_summarizing.ipynb` | Summarizing with word/focus constraints; extract vs. summarize |
| `l4_inferring.ipynb` | Sentiment, emotion, entity extraction, zero-shot topic classification |
| `l5_transforming.ipynb` | Translation, tone, format conversion, spellcheck/grammar |
| `l6_expanding.ipynb` | Generating tailored responses; temperature parameter |
| `l7_chat_format.ipynb` | Chat roles (system/user/assistant), context, OrderBot |

### Building Systems with the ChatGPT API

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
