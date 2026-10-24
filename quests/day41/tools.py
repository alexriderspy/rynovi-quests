"""Day 41 · Tool doctor

Agents fail more often because of bad tools than bad models. A tool's name, description and input schema
are the only manual the model gets. Then you check what the model sends, and when something goes wrong,
you return an error the model can act on instead of crashing.

Run `python quest.py 41` after each TODO.
"""
ORDERS = {"ORD-1042": {"status": "shipped", "items": ["notebook", "pen"]}, "ORD-2001": {"status": "processing", "items": ["bag"]}}

# TODO 41.1 · A good tool definition for searching company policies. Fill this in:
#   "name": "search_policies"
#   "description": at least 40 characters, saying what it searches and what it returns
#   "input_schema": a JSON schema object with
#       properties: "query" (type "string", with a "description") and
#                   "department" (type "string", "enum": ["hr", "it", "finance"])
#       required: ["query"]
SEARCH_POLICIES: dict = {}

GET_ORDER = {
    "name": "get_order",
    "description": "Look up one order by its id, like 'ORD-1042'. Returns its status and items.",
    "input_schema": {"type": "object", "properties": {"order_id": {"type": "string"}}, "required": ["order_id"]},
}

TYPES = {"string": str, "integer": int, "number": (int, float), "boolean": bool, "array": list, "object": dict}


def validate_args(schema: dict, args: dict) -> list[str]:
    """TODO 41.2 · Check the model's arguments against an input_schema. Return a list of problems:
      "missing <name>"            a required property is absent
      "unknown <name>"            a property the schema doesn't define
      "<name> should be <type>"   wrong type (use TYPES; note True is not an integer here)
      "<name> must be one of a, b, c"   value not in its enum
    No problems gives []."""
    raise NotImplementedError


def get_order(order_id: str) -> dict:
    """The real tool. Raises KeyError for an unknown order. Don't change it."""
    return ORDERS[order_id]


def call_get_order(args: dict) -> dict:
    """TODO 41.3 · Call get_order safely and never raise:
      - invalid args (validate_args against GET_ORDER): {"error": "; ".join(problems), "hint": "..."}
      - unknown order: {"error": "no order <id>", "hint": "check the id with the user; ids look like ORD-1042"}
      - otherwise: the order dict
    Every hint must be a non-empty sentence telling the model what to do next."""
    raise NotImplementedError
