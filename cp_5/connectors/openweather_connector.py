from connectors.base_async_connector import BaseAsyncConnector
from env_configuration import settings
from fastapi import HTTPException


class OpenWeatherConnector(BaseAsyncConnector):
    def __init__(self, city, state, country, unit, lang):
        self.city = city
        self.state = state
        self.country = country
        self.unit = unit
        self.lang = lang


    async def send_async(self):
        api_key = settings.api_key
        if self.state is not None:
            q = f"{self.city},{self.state},{self.country}"
        else:
            q = f"{self.city},{self.country}"
        try: 
            url = f"http://api.openweathermap.org/data/2.5/weather?q={q}&unit={self.unit}&lang={self.lang}&appid={api_key}"

            resp = await self.request_async(
                method="GET",
                url=url,
                timeout=settings.openweather_timeout
                )
            return resp

            # async with httpx.AsyncClient() as client:
            #     resp = await client.get(url)
            #     resp.raise_for_status()
            #     return resp

        except HTTPException as e:
            return e
