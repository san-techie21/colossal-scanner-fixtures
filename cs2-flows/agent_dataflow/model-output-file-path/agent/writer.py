import anthropic

client = anthropic.Anthropic()


def save_summary(document: str) -> None:
    reply = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=800,
        messages=[{"role": "user", "content": "First line: a file path. Then the summary.\n" + document}],
    )
    path, _, body = reply.content[0].text.partition("\n")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)
