from connectors.openweather_connector import OpenWeatherConnector
from typing import Optional


class LocationService:
    def get_report(
        city: str,
        state: Optional[str] = "FL",
        country: Optional[str] = "BR",
        unit: Optional[str] = "metric",
        lang: Optional[str] = "pt_br"
    ) -> dict:

        openweather_connector = OpenWeatherConnector(
            city=city, state=state, country=country, unit=unit, lang=lang)
        report = openweather_connector.send()

        return report
