import subprocess

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ops")
COMMANDS = {"disk": ["df", "-h"], "uptime": ["uptime"]}


@mcp.tool()
def run(name: str) -> str:
    """Run one of the known maintenance commands."""
    if name not in COMMANDS:
        raise ValueError("unknown command")
    return subprocess.run(COMMANDS[name], capture_output=True, text=True).stdout
