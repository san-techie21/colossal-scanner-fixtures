from urllib.parse import urlparse

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("docs")
ALLOWED_HOSTS = {"docs.example.com"}


@mcp.tool()
def fetch_doc(path: str) -> str:
    """Fetch a page from the documentation site."""
    url = "https://docs.example.com/" + path.lstrip("/")
    if urlparse(url).hostname not in ALLOWED_HOSTS:
        raise ValueError("host not allowed")
    return httpx.get(url, timeout=10).text
