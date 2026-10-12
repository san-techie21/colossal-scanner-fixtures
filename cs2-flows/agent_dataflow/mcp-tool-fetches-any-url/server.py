import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("web")


@mcp.tool()
def fetch_page(url: str) -> str:
    """Fetch a web page for the agent."""
    return httpx.get(url, timeout=10).text
