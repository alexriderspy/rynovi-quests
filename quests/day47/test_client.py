import asyncio
from pathlib import Path

from quests.day47.client import call, list_tool_names, tools_for_model

SERVER = str(Path(__file__).parent / "weather_server.py")


def test_47_1_discovers_tools():
    assert asyncio.run(list_tool_names(SERVER)) == ["get_weather", "to_fahrenheit"]


def test_47_2_calls_tools():
    assert asyncio.run(call(SERVER, "get_weather", {"city": "pune"})) == "Pune: 31°C"
    assert asyncio.run(call(SERVER, "to_fahrenheit", {"celsius": 38})) == "100.4"


def test_47_3_tools_for_a_model():
    tools = asyncio.run(tools_for_model(SERVER))
    assert [t["name"] for t in tools] == ["get_weather", "to_fahrenheit"]
    assert tools[0]["description"] == "Current temperature in a city, in Celsius."
    assert tools[0]["input_schema"]["required"] == ["city"]
    assert set(tools[0]) == {"name", "description", "input_schema"}
