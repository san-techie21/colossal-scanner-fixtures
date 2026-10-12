from mcp.server.fastmcp import FastMCP

mcp = FastMCP("files")


@mcp.tool()
def read_file(path: str) -> str:
    """Read a file for the agent."""
    with open(path, encoding="utf-8") as fh:
        return fh.read()
