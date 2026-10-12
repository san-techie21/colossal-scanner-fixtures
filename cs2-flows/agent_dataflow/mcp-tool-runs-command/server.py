import subprocess

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ops")


@mcp.tool()
def run(command: str) -> str:
    """Run a maintenance command."""
    return subprocess.run(command, shell=True, capture_output=True, text=True).stdout
