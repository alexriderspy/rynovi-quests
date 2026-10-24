"""Day 46 · Build an MCP server

An MCP server exposes tools (actions) and resources (data to read) to any MCP client: Claude, Cursor,
or your own agent. You write plain Python functions; FastMCP turns their signatures into schemas.

pip install "mcp<2". Try it by hand: mcp dev quests/day46/server.py  (opens the MCP Inspector)
Run `python quest.py 46` after each TODO.
"""
import json  # noqa: F401
from typing import Literal  # noqa: F401

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("rynovi-tickets")

TICKETS: dict[str, dict] = {
    "T-1": {"id": "T-1", "customer_id": "C-77", "subject": "Order never arrived", "priority": "high", "status": "open"},
    "T-2": {"id": "T-2", "customer_id": "C-77", "subject": "Change address", "priority": "low", "status": "closed"},
    "T-3": {"id": "T-3", "customer_id": "C-12", "subject": "Refund for ORD-2001", "priority": "low", "status": "open"},
}

# TODO 46.1 · A tool: @mcp.tool() on
#     def open_tickets(customer_id: str) -> list[dict]
#   with a docstring (it becomes the tool's description). Return that customer's tickets whose status is "open".

# TODO 46.2 · A tool that writes:
#     def create_ticket(customer_id: str, subject: str, priority: Literal["low", "high"] = "low") -> dict
#   Store a new open ticket with id "T-<n>" (n = number of tickets + 1) and return it.

# TODO 46.3 · A resource: @mcp.resource("tickets://{ticket_id}") on
#     def read_ticket(ticket_id: str) -> str
#   returning the ticket as a JSON string (json.dumps).

if __name__ == "__main__":
    mcp.run()
