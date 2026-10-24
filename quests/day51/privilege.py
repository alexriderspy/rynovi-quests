"""Day 51 · Least privilege

If an agent can only read, a bad prompt can't make it delete. Today: decide which tools each role may use,
keep file access inside one folder, and spot the "lethal trifecta": private data + untrusted content +
a way to send data out, all in one agent. With all three, a prompt injection can steal your data.

Run `python quest.py 51` after each TODO.
"""
from pathlib import Path

POLICY = {
    "support_agent": {"search_kb", "read_ticket", "draft_reply"},
    "billing_agent": {"read_ticket", "lookup_invoice", "refund"},
}


def allowed(role: str, tool: str) -> bool:
    """TODO 51.1 · True only if POLICY gives this role this tool. Unknown roles get nothing (deny by default)."""
    raise NotImplementedError


def safe_path(root: Path, user_path: str) -> Path:
    """TODO 51.2 · The agent asks for a file. Return the resolved path inside root, or raise PermissionError
    if it would land outside root (think "../../etc/passwd" or "/etc/passwd").
    hint: (root / user_path).resolve() and Path.is_relative_to"""
    raise NotImplementedError


def lethal_trifecta(tools: list[dict]) -> list[str]:
    """TODO 51.3 · Each tool dict may have True flags: "private_data", "untrusted_content", "external_comms".
    Return the flags the agent has, in that order, if it has ALL three (the dangerous case); otherwise return []."""
    raise NotImplementedError
