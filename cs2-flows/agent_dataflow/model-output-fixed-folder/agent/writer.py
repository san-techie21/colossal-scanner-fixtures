import re
from pathlib import Path

import anthropic

client = anthropic.Anthropic()

OUT_DIR = Path("/srv/summaries")


def save_summary(title: str, document: str) -> None:
    reply = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=800,
        messages=[{"role": "user", "content": "Summarise:\n" + document}],
    )
    name = re.sub(r"[^a-z0-9-]", "", title.lower())[:40] or "summary"
    (OUT_DIR / f"{name}.md").write_text(reply.content[0].text, encoding="utf-8")
