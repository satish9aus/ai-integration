# Building Systems with the ChatGPT API Study Guide

This folder is organized as a notebook-based study sequence for building practical LLM systems. Each lesson combines short conceptual notes with runnable examples so you can review the idea first and then inspect the implementation.

## Recommended Order

1. `l1_language_models_chat_format_tokens.ipynb`
   - foundations: chat format, tokens, and instruction tuning
2. `l2_evaluate_inputs_classification.ipynb`
   - classify incoming requests before taking action
3. `l3_evaluate_inputs_moderation.ipynb`
   - apply moderation checks to user inputs
4. `l4_process_inputs_chain_of_thought_reasoning.ipynb`
   - reason through ambiguous or multi-step requests
5. `l5_process_inputs_chaining_prompts.ipynb`
   - break complex workflows into simpler prompt stages
6. `l6_check_outputs.ipynb`
   - validate generated answers for safety and sufficiency
7. `l7_build_end_to_end_system.ipynb`
   - combine moderation, retrieval, generation, and evaluation into one pipeline
8. `l8_evaluation_part1.ipynb`
   - evaluate tasks that have a single correct answer
9. `l9_evaluation_part2.ipynb`
   - evaluate tasks where multiple answers may be acceptable

## How to Use the Notebooks

- Read the opening study notes first to understand the design pattern.
- Run the code cells section by section rather than executing everything at once.
- Pause after each lesson and write down:
  - what inputs the system expects
  - what outputs it produces
  - what failure mode the lesson is designed to address
- Compare adjacent lessons to see how the system grows from isolated prompts into a multi-step application.

## What to Focus On

- **Safety gates**: classification, moderation, and output checks
- **Control flow**: routing requests to the right next step
- **Retrieval grounding**: limiting the model to relevant product information
- **Evaluation**: measuring quality with exact matches, rubrics, and expert answers
- **System design**: turning single prompts into reliable pipelines

## Suggested Study Workflow

1. Read the study notes at the top of a notebook.
2. Skim the code once before running it.
3. Run the cells and inspect the intermediate variables.
4. Change one prompt or one example input and observe what breaks.
5. Summarize the lesson in your own words before moving on.

## Environment Notes

- The notebooks expect an `OPENAI_API_KEY` environment variable.
- Some later lessons import `utils` from a parent path. If that module is not available in your environment, those notebooks are still useful for reading the workflow design, but the import will need to be resolved before execution.
- `helper.py` contains shared helper functions used by some lessons.
