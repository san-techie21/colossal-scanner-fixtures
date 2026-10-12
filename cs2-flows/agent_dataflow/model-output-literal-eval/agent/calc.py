import ast

import anthropic

client = anthropic.Anthropic()


def numbers(question: str):
    reply = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=64,
        messages=[{"role": "user", "content": f"Return a JSON list of numbers for: {question}"}],
    )
    return ast.literal_eval(reply.content[0].text)
