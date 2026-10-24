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
HEAVY = {11, 60}  # slow quests (containers, timeouts): only checked when you play that day

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
    9: ("The job API", "quests/day09/jobs_api.py", [
        ("9.1", "List jobs, get one, 404 when it's missing"),
        ("9.2", "Create a job: validation and 201"),
        ("9.3", "Filter with a query parameter"),
        ("9.4", "Delete with 204"),
    ]),
    10: ("Invoice detective", "quests/day10/detective.py", [
        ("10.1", "Pull the text out of a PDF"),
        ("10.2", "Find the total, not the subtotal"),
        ("10.3", "Read the line-items table"),
        ("10.4", "Spot the scan"),
    ]),
    11: ("Ship it in a box", "quests/day11/Dockerfile", [
        ("11.1", "The Dockerfile builds"),
        ("11.2", "compose.yaml has the api and the database"),
        ("11.3", "The whole stack starts healthy"),
    ]),
    12: ("Agent on a leash", "quests/day12/textstats.py", [
        ("12.1", "The agent wrote a plan first"),
        ("12.2", "The tests pass"),
        ("12.3", "Tests untouched, work in small commits"),
    ]),
    14: ("Trust but verify", "quests/day14/verify.py", [
        ("14.1", "A schema for invoices"),
        ("14.2", "Parse replies, reject the broken ones"),
        ("14.3", "Check the maths in plain Python"),
        ("14.4", "Accept or send to review"),
    ]),
    29: ("Chat template by hand", "quests/day29/templates.py", [
        ("29.1", "ChatML format"),
        ("29.2", "The generation prompt"),
        ("29.3", "Llama 3 format"),
        ("29.4", "Catch malformed conversations"),
    ]),
    30: ("LoRA by hand", "quests/day30/lora.py", [
        ("30.1", "Count what LoRA trains"),
        ("30.2", "A LoRA layer that starts as a no-op"),
        ("30.3", "Merge the update into one matrix"),
        ("30.4", "The budget for a 1B model"),
    ]),
    32: ("The verdict", "quests/day32/verdict.py", [
        ("32.1", "Accuracy"),
        ("32.2", "F1 for each label"),
        ("32.3", "Macro F1"),
        ("32.4", "Pick the model to ship"),
    ]),
    33: ("Chop shop", "quests/day33/chop.py", [
        ("33.1", "Fixed-size chunks with overlap"),
        ("33.2", "Recursive chunks on paragraphs and sentences"),
        ("33.3", "Keyword search over chunks"),
        ("33.4", "Measure hit rate for both"),
    ]),
    34: ("Nearest neighbours", "quests/day34/index.py", [
        ("34.1", "Cosine similarity"),
        ("34.2", "Add and search a vector index"),
        ("34.3", "Metadata filters"),
        ("34.4", "Delete"),
    ]),
    35: ("Best of both", "quests/day35/fusion.py", [
        ("35.1", "Reciprocal rank fusion"),
        ("35.2", "Hit rate at k"),
        ("35.3", "Hybrid beats both"),
    ]),
    36: ("Show your sources", "quests/day36/sources.py", [
        ("36.1", "Find the citations"),
        ("36.2", "Catch fake and missing citations"),
        ("36.3", "Refuse on weak retrieval"),
        ("36.4", "What users actually see"),
    ]),
    37: ("Golden set", "quests/day37/golden.py", [
        ("37.1", "A schema and a loader for test cases"),
        ("37.2", "Coverage and gaps"),
        ("37.3", "Grow golden.jsonl until it's good enough"),
    ]),
    38: ("Judge the judge", "quests/day38/judge.py", [
        ("38.1", "Confusion counts"),
        ("38.2", "Agreement"),
        ("38.3", "True positive and negative rates"),
        ("38.4", "Pick the judge"),
    ]),
    40: ("The loop", "quests/day40/loop.py", [("40.1", "Run a tool without crashing"), ("40.2", "The agent loop"), ("40.3", "A step limit")]),
    41: ("Tool doctor", "quests/day41/tools.py", [("41.1", "A good tool definition"), ("41.2", "Validate the model's arguments"), ("41.3", "Errors the model can act on")]),
    42: ("State vs memory", "quests/day42/state.py", [("42.1", "Structured state"), ("42.2", "Trim history to a budget"), ("42.3", "State survives trimming")]),
    43: ("Remember me", "quests/day43/memory.py", [("43.1", "Remember, replace, forget"), ("43.2", "Recall what's relevant"), ("43.3", "Extract facts from messages")]),
    44: ("Graph it", "quests/day44/graph.py", [("44.1", "The nodes"), ("44.2", "Wire the graph with a conditional edge"), ("44.3", "Pause and resume from a checkpoint")]),
    46: ("Build an MCP server", "quests/day46/server.py", [("46.1", "A read tool"), ("46.2", "A write tool with an enum"), ("46.3", "A resource")]),
    47: ("Plug in", "quests/day47/client.py", [("47.1", "Discover a server's tools"), ("47.2", "Call them"), ("47.3", "Hand them to a model")]),
    48: ("Context budget", "quests/day48/context.py", [("48.1", "Pinned, old and recent"), ("48.2", "Compress with a summary"), ("48.3", "30 steps under budget")]),
    49: ("Approval gate", "quests/day49/approvals.py", [("49.1", "What needs a person"), ("49.2", "Pause at risky calls"), ("49.3", "Approve, edit, reject, resume")]),
    50: ("Rails", "quests/day50/rails.py", [("50.1", "Redact Aadhaar, PAN, phone, email"), ("50.2", "Step and cost limits"), ("50.3", "Check drafts before they're sent")]),
    51: ("Least privilege", "quests/day51/privilege.py", [("51.1", "Tool allow-list"), ("51.2", "Folder sandbox"), ("51.3", "Spot the lethal trifecta")]),
    52: ("Read the trace", "quests/day52/read_trace.py", [("52.1", "The slowest step"), ("52.2", "Cost per run"), ("52.3", "What broke, and where")]),
    53: ("Open coding", "quests/day53/open_coding.py", [("53.1", "Count failures by category"), ("53.2", "Where to focus"), ("53.3", "Real examples for the team")]),
    54: ("Grow the set", "quests/day54/grow.py", [("54.1", "Normalise inputs"), ("54.2", "Add new cases, skip duplicates"), ("54.3", "Version the set")]),
    55: ("Calibrate the judge", "quests/day55/calibrate.py", [("55.1", "TPR and TNR"), ("55.2", "Does it hold up on test?"), ("55.3", "Correct the production pass rate")]),
    56: ("Score the trajectory", "quests/day56/trajectory.py", [("56.1", "Task success"), ("56.2", "Right tools, right order"), ("56.3", "Wasted steps and a report")]),
    57: ("Cheap checks first", "quests/day57/checks.py", [("57.1", "Code checks"), ("57.2", "Route to the judge"), ("57.3", "Money saved")]),
    58: ("Regression gate", "quests/day58/gate.py", [("58.1", "Find the drops"), ("58.2", "A CI command that fails the build"), ("58.3", "Move the baseline forward")]),
    60: ("Stream it", "quests/day60/app.py", [("60.1", "Health check"), ("60.2", "Stream tokens as server-sent events"), ("60.3", "Time out slow requests")]),
    63: ("Cost dashboard", "quests/day63/dashboard.py", [("63.1", "p50 and p95 latency"), ("63.2", "Cost per task"), ("63.3", "The costliest step")]),
    64: ("Gateway", "quests/day64/gateway.py", [("64.1", "Fall back when a model fails"), ("64.2", "Cache repeat questions"), ("64.3", "Load test it")]),
    67: ("Who sees what", "quests/day67/access.py", [("67.1", "Can this user read it?"), ("67.2", "Filter before ranking"), ("67.3", "Audit log")]),
    68: ("Connector", "quests/day68/connector.py", [("68.1", "Every page"), ("68.2", "Respect the rate limit"), ("68.3", "Index with permissions")]),
    69: ("Fresh index", "quests/day69/sync.py", [("69.1", "Content hashes"), ("69.2", "Plan the sync"), ("69.3", "Embed only what changed")]),
    70: ("Change data capture", "quests/day70/cdc.py", [("70.1", "Apply one change"), ("70.2", "Replay safely"), ("70.3", "Resume after a crash")]),
    71: ("Where does data go", "quests/day71/scan.py", [("71.1", "Spot personal data"), ("71.2", "Scan a project"), ("71.3", "Clean it up")]),
    73: ("No leaks", "quests/day73/leaks.py", [("73.1", "Find images and links"), ("73.2", "Spot exfiltration and secrets"), ("73.3", "Make it safe to render")]),
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
        mine = {k: v for k, v in res.items() if k.startswith("test_" + level.replace(".", "_") + "_")}
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
    for day, (name, _, levels) in QUESTS.items():
        if day in HEAVY:
            print(f"    Day {day:>2}  {name:<24} {DIM}check it with python quest.py {day}{END}")
            total += len(levels)
            continue
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
