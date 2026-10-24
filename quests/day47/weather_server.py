"""The MCP server you'll connect to on day 47. Don't edit this file; it runs as its own process."""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("rynovi-weather")
TEMPS = {"pune": 31, "delhi": 38, "bengaluru": 26, "chennai": 34}


@mcp.tool()
def get_weather(city: str) -> str:
    """Current temperature in a city, in Celsius."""
    t = TEMPS.get(city.lower())
    return f"{city.title()}: {t}°C" if t is not None else f"No data for {city}"


@mcp.tool()
def to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return round(celsius * 9 / 5 + 32, 1)


if __name__ == "__main__":
    mcp.run()
