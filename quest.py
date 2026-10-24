"""Rynovi quests: small coding levels that go with each day of the Rynovi roadmap.

    python quest.py          show every quest and your XP
    python quest.py 3        play day 3: run its levels and point you at the next TODO
"""
import os
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).parent
XP_PER_LEVEL = 10

GREEN, RED, GOLD, DIM, BOLD, END = ("\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[1m", "\033[0m") if sys.stdout.isatty() else ("",) * 6

# day: (name, file you edit, [(level, what it checks)])
QUESTS = {
    2: ("The job board bouncer", "quests/day02/job_board.py", [
        ("2.1", "Fields, types and defaults"),
        ("2.2", "Clean up titles with a field validator"),
        ("2.3", "On-site jobs need a location (model validator)"),
        ("2.4", "Split good records from bad, with clear errors"),
    ]),
    3: ("The speed run", "quests/day03/speed_run.py", [
        ("3.1", "Fetch one page with await"),
        ("3.2", "Fetch 20 pages at once with gather"),
        ("3.3", "Never more than 3 at once (Semaphore)"),
        ("3.4", "Don't wait for pages that hang (timeouts)"),
    ]),
    4: ("The flaky server", "quests/day04/flaky_server.py", [
        ("4.1", "Retry with exponential backoff"),
        ("4.2", "Fail fast on errors that won't go away"),
        ("4.3", "Log every retry"),
    ]),
    5: ("Bug hunt", "quests/day05/test_my_cart.py", [
        ("5.0", "Your tests pass on the real cart"),
        ("5.1", "Catch bug 1"),
        ("5.2", "Catch bug 2"),
        ("5.3", "Catch bug 3"),
    ]),
}


def run_pytest(path: str, env_extra: dict | None = None) -> dict[str, tuple[bool, str]]:
    """Run pytest on a folder and return {test name: (passed, first line of the failure)}."""
    with tempfile.NamedTemporaryFile(suffix=".xml", delete=False) as f:
        report = f.name
    env = {**os.environ, **(env_extra or {}), "PYTHONDONTWRITEBYTECODE": "1"}
    subprocess.run([sys.executable, "-m", "pytest", path, "-q", "-p", "no:cacheprovider", f"--junitxml={report}"],
                   cwd=ROOT, env=env, capture_output=True, text=True)
    results: dict[str, tuple[bool, str]] = {}
    try:
        for case in ET.parse(report).getroot().iter("testcase"):
            bad = case.find("failure") if case.find("failure") is not None else case.find("error")
            msg = (bad.get("message") or "").strip().splitlines()[0][:160] if bad is not None else ""
            results[case.get("name", "")] = (bad is None, msg)
    finally:
        os.unlink(report)
    return results


def check(day: int) -> list[tuple[str, str, bool, str]]:
    name, file, levels = QUESTS[day]
    folder = str(Path(file).parent)
    if day == 5:
        mine = run_pytest(folder)
        ok = bool(mine) and all(p for p, _ in mine.values())
        why = next((m for p, m in mine.values() if not p), "write at least one test")
        out = [("5.0", levels[0][1], ok, "" if ok else why)]
        for i in (1, 2, 3):
            res = run_pytest(folder, {"RYNOVI_CART": f"quests.day05._bugs.bug{i}"})
            caught = ok and any(not p for p, _ in res.values())
            out.append((f"5.{i}", levels[i][1], caught, "" if caught else "all your tests still pass on the buggy cart"))
        return out
    res = run_pytest(folder)
    out = []
    for level, what in levels:
        mine = {k: v for k, v in res.items() if k.startswith("test_" + level.replace(".", "_"))}
        ok = bool(mine) and all(p for p, _ in mine.values())
        why = next((m for p, m in mine.values() if not p), "")
        out.append((level, what, ok, why))
    return out


def bar(done: int, total: int, width: int = 24) -> str:
    n = round(width * done / total) if total else 0
    return GOLD + "█" * n + DIM + "░" * (width - n) + END


def play(day: int) -> None:
    name, file, _ = QUESTS[day]
    print(f"\n{BOLD}Day {day} · {name}{END}   {DIM}edit {file}{END}\n")
    results = check(day)
    for level, what, ok, why in results:
        if ok:
            print(f"  {GREEN}✔ {level}{END}  {what}  {DIM}+{XP_PER_LEVEL} XP{END}")
        else:
            print(f"  {RED}✘ {level}{END}  {what}")
            if why:
                print(f"         {DIM}{why}{END}")
    done = sum(ok for *_, ok, _ in results)
    print(f"\n  {bar(done, len(results))}  {done}/{len(results)} levels · {done * XP_PER_LEVEL} XP")
    nxt = next((r for r in results if not r[2]), None)
    if nxt:
        print(f"\n  Next: {BOLD}TODO {nxt[0]}{END} in {file}, then run python quest.py {day} again.\n")
    else:
        print(f"\n  {GREEN}{BOLD}Day {day} cleared!{END} Tick off today's Play task in Rynovi.\n")


def overview() -> None:
    print(f"\n{BOLD}Rynovi quests{END}\n")
    total = xp = 0
    for day, (name, _, _) in QUESTS.items():
        results = check(day)
        done = sum(ok for *_, ok, _ in results)
        total += len(results)
        xp += done * XP_PER_LEVEL
        mark = f"{GREEN}✔{END}" if done == len(results) else " "
        print(f"  {mark} Day {day:>2}  {name:<24} {bar(done, len(results), 12)} {done}/{len(results)}")
    print(f"\n  {xp} / {total * XP_PER_LEVEL} XP · play one with python quest.py <day>\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        d = int(sys.argv[1])
        if d not in QUESTS:
            sys.exit(f"No quest for day {d} yet. Quests so far: days {', '.join(map(str, QUESTS))}.")
        play(d)
    else:
        overview()
