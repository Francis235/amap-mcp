import os
import requests

from dotenv import load_dotenv
load_dotenv()

def query_weather():
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    request_data = {
        "city": 110101,
        "key": os.getenv("AMAP_KEY")
    }
    response = requests.get(url, params=request_data)
    print(response.json())

if __name__ == "__main__":
    query_weather()