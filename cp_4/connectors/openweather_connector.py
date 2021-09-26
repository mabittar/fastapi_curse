from connectors.base_connector import BaseConnector
from env_configuration import settings
from fastapi import HTTPException

class OpenWeatherConnector(BaseConnector):
    def __init__(self, city, state, country, unit, lang):
        self.city = city
        self.state = state
        self.country = country
        self.unit = unit
        self.lang = lang


    def send(self):
        api_key = settings.api_key
        if self.state is not None:
            q = f"{self.city},{self.state},{self.country}"
        else:
            q = f"{self.city},{self.country}"
        try: 
            url = f"http://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&unit={self.unit}&lang={self.lang}"

            resp = self.request(
                method="GET",
                url=url
                )
            return resp

        except HTTPException as e:
            return e
