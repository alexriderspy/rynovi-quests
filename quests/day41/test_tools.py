from quests.day41.tools import GET_ORDER, SEARCH_POLICIES, call_get_order, validate_args


def test_41_1_good_tool_definition():
    t = SEARCH_POLICIES
    assert t.get("name") == "search_policies"
    assert len(t.get("description", "")) >= 40, "describe what it searches and what it returns"
    s = t.get("input_schema", {})
    assert s.get("type") == "object" and s.get("required") == ["query"]
    assert s["properties"]["query"]["type"] == "string" and s["properties"]["query"].get("description")
    assert s["properties"]["department"]["enum"] == ["hr", "it", "finance"]


def test_41_2_validation():
    schema = SEARCH_POLICIES["input_schema"]
    assert validate_args(schema, {"query": "leave", "department": "hr"}) == []
    assert validate_args(schema, {"department": "hr"}) == ["missing query"]
    assert validate_args(schema, {"query": 42}) == ["query should be string"]
    assert validate_args(schema, {"query": "x", "department": "sales"}) == ["department must be one of hr, it, finance"]
    assert validate_args(schema, {"query": "x", "limit": 5}) == ["unknown limit"]


def test_41_2_bool_is_not_an_integer():
    schema = {"type": "object", "properties": {"n": {"type": "integer"}}, "required": ["n"]}
    assert validate_args(schema, {"n": True}) == ["n should be integer"]
    assert validate_args(schema, {"n": 3}) == []


def test_41_3_errors_the_model_can_act_on():
    assert call_get_order({"order_id": "ORD-1042"})["status"] == "shipped"
    bad = call_get_order({"order_id": "ORD-9"})
    assert bad["error"] == "no order ORD-9" and len(bad["hint"]) > 10
    bad = call_get_order({"id": "ORD-1042"})
    assert "missing order_id" in bad["error"] and "unknown id" in bad["error"] and bad["hint"]
