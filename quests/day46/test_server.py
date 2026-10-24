import asyncio
import json

from mcp.shared.memory import create_connected_server_and_client_session

from quests.day46 import server


def run(coro_fn):
    async def go():
        async with create_connected_server_and_client_session(server.mcp._mcp_server) as client:
            return await coro_fn(client)
    return asyncio.run(go())


def payload(result):
    if getattr(result, "structuredContent", None):
        sc = result.structuredContent
        return sc.get("result", sc)
    return json.loads(result.content[0].text)


def test_46_1_open_tickets_tool():
    async def go(c):
        tools = {t.name: t for t in (await c.list_tools()).tools}
        assert "open_tickets" in tools, "decorate open_tickets with @mcp.tool()"
        assert tools["open_tickets"].description, "give it a docstring"
        assert tools["open_tickets"].inputSchema["required"] == ["customer_id"]
        return payload(await c.call_tool("open_tickets", {"customer_id": "C-77"}))
    assert [t["id"] for t in run(go)] == ["T-1"]


def test_46_2_create_ticket_tool():
    async def go(c):
        tools = {t.name: t for t in (await c.list_tools()).tools}
        assert tools["create_ticket"].inputSchema["properties"]["priority"]["enum"] == ["low", "high"]
        made = payload(await c.call_tool("create_ticket", {"customer_id": "C-12", "subject": "Wrong item"}))
        still = payload(await c.call_tool("open_tickets", {"customer_id": "C-12"}))
        return made, still
    made, still = run(go)
    assert made["id"] == "T-4" and made["priority"] == "low" and made["status"] == "open"
    assert {t["id"] for t in still} == {"T-3", "T-4"}
    server.TICKETS.pop("T-4", None)


def test_46_3_ticket_resource():
    async def go(c):
        res = await c.read_resource("tickets://T-3")
        return json.loads(res.contents[0].text)
    assert run(go)["subject"] == "Refund for ORD-2001"
