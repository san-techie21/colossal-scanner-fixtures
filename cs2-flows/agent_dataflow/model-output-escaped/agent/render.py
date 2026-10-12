import anthropic
from markupsafe import Markup, escape

client = anthropic.Anthropic()


def summary_html(document: str) -> Markup:
    reply = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=600,
        messages=[{"role": "user", "content": "Summarise:\n" + document}],
    )
    return Markup("<p>{}</p>").format(escape(reply.content[0].text))
