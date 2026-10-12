import subprocess

import anthropic

client = anthropic.Anthropic()
ALLOWED = {"restart": ["systemctl", "restart", "app"], "status": ["systemctl", "status", "app"]}


def run_suggested_action(issue: str) -> str:
    reply = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=16,
        messages=[{"role": "user", "content": f"Answer restart or status for: {issue}"}],
    )
    action = reply.content[0].text.strip().lower()
    if action not in ALLOWED:
        raise ValueError("the model proposed an action outside the allow-list")
    result = subprocess.run(ALLOWED[action], capture_output=True, text=True, check=False)
    return result.stdout
