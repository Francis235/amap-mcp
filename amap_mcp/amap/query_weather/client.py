import requests
import httpx
import logging
import typing

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AmapQueryWeatherClient:
    def __init__(self, key: str, httpx_client: typing.Union[httpx.Client, httpx.AsyncClient]):
        self.key = key
        self.httpx_client = httpx_client

    def query_weather_impl(self, city: str):
        url = "https://restapi.amap.com/v3/weather/weatherInfo"
        request_data = {
            "city": city,
            "key": self.key
        }
        response = requests.get(url, params=request_data)
        return response.json()
    
    async def async_query_weather_impl(self, city: str):
        url = "https://restapi.amap.com/v3/weather/weatherInfo"
        request_data = {
            "city": city,
            "key": self.key
        }
        logger.info(f"request_data: {request_data}")
        try:
            response = await self.httpx_client.get(url, params=request_data)
            return response.json()
        except Exception as e:
            logger.error(f"error: {e}")
            raise e
