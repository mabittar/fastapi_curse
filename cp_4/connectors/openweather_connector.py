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

        q = {self.country, self.state, self.city}
        try: 
            url = f"http://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&unit={self.unit}&lang={self.lang}"

            resp = self.request(
                method="POST",
                url=url
                )
            return resp

        except HTTPException as e:
            return e
