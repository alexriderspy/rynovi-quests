"""One run of the service copilot, as spans from a tracer. Don't edit this file.
Times are in milliseconds from the start of the run."""

TRACE = [
    {'id': 's0', 'parent': None, 'name': 'copilot_run', 'kind': 'chain', 'start_ms': 0, 'end_ms': 9400},
    {'id': 's1', 'parent': 's0', 'name': 'classify_email', 'kind': 'llm', 'model': 'small', 'start_ms': 10, 'end_ms': 620, 'tokens_in': 800, 'tokens_out': 20},
    {'id': 's2', 'parent': 's0', 'name': 'plan', 'kind': 'llm', 'model': 'large', 'start_ms': 640, 'end_ms': 2900, 'tokens_in': 3200, 'tokens_out': 400},
    {'id': 's3', 'parent': 's2', 'name': 'search_manuals', 'kind': 'tool', 'start_ms': 2950, 'end_ms': 3600},
    {'id': 's4', 'parent': 's2', 'name': 'lookup_order', 'kind': 'tool', 'start_ms': 2960, 'end_ms': 3100, 'error': '404 order not found'},
    {'id': 's5', 'parent': 's0', 'name': 'draft_reply', 'kind': 'llm', 'model': 'large', 'start_ms': 3650, 'end_ms': 8900, 'tokens_in': 9000, 'tokens_out': 700},
    {'id': 's6', 'parent': 's0', 'name': 'check_draft', 'kind': 'llm', 'model': 'small', 'start_ms': 8920, 'end_ms': 9380, 'tokens_in': 1200, 'tokens_out': 30},
]

# Rupees per million tokens.
PRICES = {"small": {"in": 80, "out": 320}, "large": {"in": 250, "out": 1250}}
