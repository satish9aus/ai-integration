# Course Introduction: ChatGPT Prompt Engineering for Developers

## Overview

This course is for developers who want to use ChatGPT and similar models in software. It focuses on building real applications with API calls, not just using the ChatGPT web page.

## Instructors

- **Isa Fulford**: OpenAI technical staff member, creator of the ChatGPT Retrieval plugin, and contributor to the OpenAI Cookbook.
- **Course host**: A member of AI Fund / DeepLearning.ai who helps startups use LLM APIs in real products.

## What this introduction says

- The course teaches prompt engineering for software development.
- Many online prompt guides are about the ChatGPT web interface and one-off tasks.
- The real power of these models is using APIs to build software quickly.
- The course recommends using instruction-tuned LLMs for most applications.
- The course covers:
  - prompt best practices for developers
  - common tasks like summarizing, inferring, transforming, and expanding text
  - building a chatbot with an LLM
- The examples come from real startup work with LLM applications.
- Instruction-tuned models are usually easier and safer than base models.

## Base LLMs vs instruction-tuned LLMs

- **Base LLMs** predict the next word in text. They are trained on large amounts of data, but they may not follow instructions well.
- **Instruction-tuned LLMs** are trained to follow directions and give helpful answers.
- Example:
  - A base LLM might continue "What is the capital of France" with unrelated text.
  - An instruction-tuned model is more likely to answer "The capital of France is Paris."
- Instruction-tuned models often get extra training with human feedback to make them more helpful and safe.

## Simple prompting advice

- Think of prompting like giving clear instructions to a smart assistant.
- Say exactly what you want, including the topic, tone, and format.
- Give the model any important context or text it should use.
- If the model does not do what you want, it usually means the instructions were not clear enough.

## Acknowledgements

This course was created with help from OpenAI and DeepLearning.ai team members:

- OpenAI: Andrew Mayne, Joe Palermo, Boris Power, Ted Sanders, Lillian Weng
- DeepLearning.ai: Geoff Lodwig, Eddy Shyu, Tommy Nelson
