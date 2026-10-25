<div align="center">

# Rynovi mini-projects

**45 small, real AI-engineering projects, built alongside the [Rynovi](https://rynovi.vercel.app) 90-day plan.**

Each one starts with a brief from a (made-up) team that needs something built, and ends with working, tested code on your own GitHub.

</div>

## How it works

1. **Fork this repo** (the Fork button, top right). Your fork is your portfolio: every mini-project you finish lives there.
2. **Clone your fork** and set it up once:

   ```bash
   git clone https://github.com/<your-username>/rynovi-quests.git
   cd rynovi-quests
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **On a mini-project day**, open that day's folder and read its `README.md`: the brief, what you'll build, and what "done" means.
4. **Build it.** Fill in the `TODO`s, then run the checks until everything is green:

   ```bash
   python quest.py 9    # check day 9's mini-project, and see what to do next
   python quest.py      # see all 45 and your progress
   ```

5. **Ship it.** Commit, push, and add a line under **My mini-projects** below.

## My mini-projects

<!-- Fill this in as you go. Recruiters who open your fork read this first. For example:
- **Day 9 · Jobs API for a hiring board**: FastAPI service with validation and proper status codes. [code](quests/day09)
-->

_Nothing here yet. Your first one is on day 2._

## All 45, by stage

### Foundations · days 1 to 14

| Day | Mini-project | You'll practise | Time |
|---|---|---|---|
| 2 | [Validator for scraped job postings](quests/day02) | Pydantic models, field and model validators, collecting errors | ~35 min |
| 3 | [Concurrent page fetcher with asyncio](quests/day03) | `async`/`await`, `asyncio.gather`, semaphores, timeouts | ~35 min |
| 4 | [Retry wrapper for a flaky API](quests/day04) | Retries, exponential backoff, failing fast, logging | ~30 min |
| 5 | [Test suite for a shopping cart](quests/day05) | Writing pytest tests that catch 3 planted bugs | ~35 min |
| 9 | [Jobs API for a hiring board](quests/day09) | FastAPI endpoints, status codes, validation, query parameters | ~35 min |
| 10 | [Invoice reader for PDFs](quests/day10) | Reading text and tables from PDFs, spotting scans | ~35 min |
| 11 | [Dockerised API with Postgres](quests/day11) | A Dockerfile and a compose.yaml for an API with Postgres (needs Docker running) | ~40 min |
| 12 | [Text stats module, built by an agent](quests/day12) | Working with a coding agent: plan first, small reviewed commits, tests untouched. Free local setup: [local-coding-agent](https://github.com/alexriderspy/local-coding-agent) | ~45 min |
| 14 | [Checker for model-extracted invoices](quests/day14) | Schemas for model output, checking the maths, routing to review | ~35 min |

### LLM engineering · days 28 to 39

| Day | Mini-project | You'll practise | Time |
|---|---|---|---|
| 29 | [Chat templates by hand](quests/day29) | ChatML and Llama 3 formats, generation prompts, valid conversations | ~30 min |
| 30 | [LoRA from scratch](quests/day30) | A LoRA layer in NumPy, parameter counts, merging | ~45 min |
| 32 | [Ship-or-not report for a fine-tune](quests/day32) | Accuracy vs per-label F1 vs cost: should you ship the fine-tune? | ~30 min |
| 33 | [Chunkers for a handbook assistant](quests/day33) | Fixed and recursive chunking, measuring hit rate | ~35 min |
| 34 | [Vector index for handbook search](quests/day34) | A tiny vector index: cosine, top-k, metadata filters | ~30 min |
| 35 | [Hybrid search for a support bot](quests/day35) | Hybrid search with reciprocal rank fusion | ~30 min |
| 36 | [Citation checker for an HR assistant](quests/day36) | Checking citations and refusing on weak retrieval | ~30 min |
| 37 | [Golden set for a handbook bot](quests/day37) | Validating and growing an eval set | ~40 min |
| 38 | [Picking an LLM judge you trust](quests/day38) | Agreement vs true positive and negative rates for LLM judges | ~30 min |

### Agents · days 40 to 52

| Day | Mini-project | You'll practise | Time |
|---|---|---|---|
| 40 | [Agent loop from scratch](quests/day40) | The agent loop: tool calls, results, step limits | ~30 min |
| 41 | [Fixing tools for an order agent](quests/day41) | Tool schemas, argument validation, actionable errors | ~35 min |
| 42 | [State and history for support chat](quests/day42) | Structured state and trimming history to a budget | ~30 min |
| 43 | [Long-term memory for a career bot](quests/day43) | Long-term memory: save, recall, replace, forget | ~30 min |
| 44 | [LangGraph router with checkpoints](quests/day44) | LangGraph: nodes, conditional edges, checkpoints | ~40 min |
| 46 | [MCP server for support tickets](quests/day46) | Tools and resources with the MCP Python SDK | ~35 min |
| 47 | [MCP client for a weather server](quests/day47) | An MCP client over stdio, tools handed to a model | ~35 min |
| 48 | [Context budget for a research agent](quests/day48) | Trimming and summarising long runs | ~30 min |
| 49 | [Approval gate for refunds](quests/day49) | Human-in-the-loop with resumable checkpoints | ~30 min |
| 50 | [Guardrails for a support bot](quests/day50) | PII redaction, step and cost limits, draft checks | ~30 min |
| 51 | [Least-privilege tools for agents](quests/day51) | Allow-lists, folder sandboxes, the lethal trifecta | ~35 min |
| 52 | [Trace reader for a copilot run](quests/day52) | Latency, cost and failures from a trace | ~30 min |

### Evals and production · days 53 to 65

| Day | Mini-project | You'll practise | Time |
|---|---|---|---|
| 53 | [Error analysis for an HR bot](quests/day53) | Error analysis: categorise failures and find the biggest | ~30 min |
| 54 | [A golden set that grows](quests/day54) | Growing a versioned golden set without duplicates | ~30 min |
| 55 | [Calibrate an LLM judge](quests/day55) | Judge rates on held-out data, corrected pass rates | ~30 min |
| 56 | [Trajectory scores for agent runs](quests/day56) | Agent evals: success, tool order, wasted steps | ~30 min |
| 57 | [Cheap checks before the judge](quests/day57) | Code-based checks before LLM judges | ~30 min |
| 58 | [Eval regression gate for CI](quests/day58) | A CI gate that fails when scores drop | ~30 min |
| 60 | [Streaming chat endpoint with FastAPI](quests/day60) | FastAPI streaming (SSE), health checks, timeouts | ~30 min |
| 63 | [Cost dashboard for a copilot](quests/day63) | p50/p95 latency, cost per task, costliest step | ~30 min |
| 64 | [Model gateway with fallback and cache](quests/day64) | Fallbacks, caching and a load test | ~35 min |

### Enterprise integration · days 66 to 75

| Day | Mini-project | You'll practise | Time |
|---|---|---|---|
| 67 | [Permission-aware search with audit log](quests/day67) | Permission-aware retrieval and audit logs | ~30 min |
| 68 | [Paginated document connector](quests/day68) | Pagination, rate limits, permissions | ~35 min |
| 69 | [Incremental index sync](quests/day69) | Incremental indexing with content hashes | ~30 min |
| 70 | [CDC replay into a table](quests/day70) | Replaying change streams safely | ~30 min |
| 71 | [PII scanner for project files](quests/day71) | Finding and cleaning PII in logs, traces and evals | ~30 min |
| 73 | [Output filter against data leaks](quests/day73) | Blocking exfiltration via images, links and secrets | ~30 min |

## Stuck?

More than 10 minutes on one TODO? Re-watch today's clip in the app, then try again. Don't peek in `quests/day05/_bugs` until you've caught them.
