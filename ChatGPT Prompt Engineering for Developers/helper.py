"""Helper functions for interacting with the OpenAI API."""

import os
import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_completion(prompt, model="gpt-3.5-turbo"):
    """Get completion from OpenAI API for a given prompt."""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return response.choices[0].message.content


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    """Get completion from OpenAI API for a list of messages."""
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content
