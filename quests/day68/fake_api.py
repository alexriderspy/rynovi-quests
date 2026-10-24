"""A pretend document API, like Google Drive or SharePoint. Don't edit this file.

list_files(page_token) returns {"files": [...], "next_page_token": str | None}, 2 files per page.
After 4 calls without a pause it raises RateLimited; call wait() to pause (the limit resets).
"""


class RateLimited(Exception):
    pass


FILES = [
    {"id": f"f{i}", "title": t, "trashed": tr, "permissions": p}
    for i, (t, tr, p) in enumerate([
        ("Leave policy", False, ["everyone"]), ("Salary bands", False, ["hr"]), ("Old draft", True, ["everyone"]),
        ("VPN guide", False, ["everyone"]), ("Board notes", False, ["leadership"]), ("Travel policy", False, ["everyone"]),
        ("Incident report", False, ["it"]), ("Temp notes", True, ["it"]), ("Learning budget", False, ["everyone"]),
        ("Laptop policy", False, ["everyone", "it"]), ("Offsite plan", False, ["leadership", "hr"]),
    ], start=1)
]


class FakeDrive:
    def __init__(self) -> None:
        self.calls = 0
        self.since_wait = 0
        self.waits = 0

    def wait(self) -> None:
        self.waits += 1
        self.since_wait = 0

    def list_files(self, page_token: str | None = None) -> dict:
        self.calls += 1
        self.since_wait += 1
        if self.since_wait > 4:
            raise RateLimited("slow down")
        start = int(page_token or 0)
        page = FILES[start:start + 2]
        nxt = str(start + 2) if start + 2 < len(FILES) else None
        return {"files": [dict(f) for f in page], "next_page_token": nxt}
