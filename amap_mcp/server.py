import logging
import httpx
import os
import amap_mcp
from amap_mcp.amap import AmapClient

from amap_mcp.amap import AmapClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"amap-mcp version: {amap_mcp.__version__}")

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from amap_mcp.amap import AmapClient

load_dotenv()
amap_key = os.getenv("AMAP_KEY")
if not amap_key:
    raise ValueError("AMAP_KEY environment variable is required")

# increase timeout for async client
async_custom_client = httpx.AsyncClient(
    timeout=httpx.Timeout(30.0, connect=60.0, read=30.0)
)

# async client instance
async_client = AmapClient(
    key = amap_key,
    httpx_client = async_custom_client
)

mcp = FastMCP("AMap")

@mcp.tool(
    description="""The weather service of Amap. Query the weather of a given city.
    
    Args:
        city (str): The city to query the weather.
    """
)
async def query_weather(city: str):
    logger.info(f"query_weather is called.")
    return await async_client.async_query_weather(city)

def main():
    logger.info("Starting MCP server")
    mcp.run()


if __name__ == "__main__":
    main()