import anthropic
from markupsafe import Markup

client = anthropic.Anthropic()


def summary_html(document: str) -> Markup:
    reply = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=600,
        messages=[{"role": "user", "content": "Summarise as HTML:\n" + document}],
    )
    return Markup(reply.content[0].text)
