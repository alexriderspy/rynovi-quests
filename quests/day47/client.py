"""Day 47 · Plug in

The other half of MCP: your code is the client. It starts a server as a separate process, talks to it
over stdio, discovers its tools and calls them. Then it hands those tools to a model.

pip install "mcp<2". Use:
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
Start the server with StdioServerParameters(command=sys.executable, args=[server_path]),
and always `await session.initialize()` first.

Run `python quest.py 47` after each TODO.
"""
import sys  # noqa: F401

from mcp import ClientSession, StdioServerParameters  # noqa: F401
from mcp.client.stdio import stdio_client  # noqa: F401


async def list_tool_names(server_path: str) -> list[str]:
    """TODO 47.1 · Connect, initialize, list the tools, and return their names sorted."""
    raise NotImplementedError


async def call(server_path: str, name: str, args: dict) -> str:
    """TODO 47.2 · Call one tool and return the text of the first content block of the result."""
    raise NotImplementedError


async def tools_for_model(server_path: str) -> list[dict]:
    """TODO 47.3 · Turn the server's tools into the format the Claude API expects:
        {"name": ..., "description": ..., "input_schema": <the tool's inputSchema>}
    sorted by name."""
    raise NotImplementedError
