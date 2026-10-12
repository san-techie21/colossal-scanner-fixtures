import shlex
import subprocess

import anthropic

client = anthropic.Anthropic()


def run_suggested_fix(issue: str) -> str:
    reply = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=512,
        messages=[{"role": "user", "content": f"Give one shell command that fixes: {issue}"}],
    )
    command = reply.content[0].text
    result = subprocess.run(shlex.split(command), capture_output=True, text=True, check=False)
    return result.stdout
