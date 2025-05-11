import httpx
import typing
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from .query_weather.client import AmapQueryWeatherClient

class AmapClient:
    def __init__(self, key: str, httpx_client: typing.Union[httpx.Client, httpx.AsyncClient]):
        self.key = key
        self.httpx_client = httpx_client
        self.query_weather_client = AmapQueryWeatherClient(key, httpx_client)

    def query_weather(self, city: str):
        return self.query_weather_client.query_weather_impl(city)
    
    async def async_query_weather(self, city: str):
        return await self.query_weather_client.async_query_weather_impl(city)
