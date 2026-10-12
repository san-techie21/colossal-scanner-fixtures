import anthropic

client = anthropic.Anthropic()


def compute(question: str):
    reply = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=64,
        messages=[{"role": "user", "content": f"Write a Python expression for: {question}"}],
    )
    return eval(reply.content[0].text)
