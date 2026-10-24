"""Day 68 · Connector

Company documents live behind APIs that return one page at a time and push back when you call too fast.
A good connector gets everything, respects the rate limit, and keeps each document's permissions.

Run `python quest.py 68` after each TODO.
"""
from quests.day68.fake_api import FakeDrive, RateLimited  # noqa: F401


def fetch_all(api: FakeDrive) -> list[dict]:
    """TODO 68.1 · Follow next_page_token until it's None and return every file, in order.

    TODO 68.2 · When list_files raises RateLimited, call api.wait() and retry the SAME page. Never skip a page."""
    raise NotImplementedError


def to_index(files: list[dict]) -> list[dict]:
    """TODO 68.3 · What goes into the search index: skip trashed files, and keep only
    {"id", "title", "allowed": sorted permissions}. A document without its permissions must never be indexed."""
    raise NotImplementedError
