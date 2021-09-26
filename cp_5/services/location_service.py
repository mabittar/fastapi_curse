from connectors.openweather_connector import OpenWeatherConnector
from typing import Optional
from infrastructure import weather_cache

class LocationService:
    async def get_report_async(
        city: str,
        state: Optional[str] = None,
        country: Optional[str] = "BR",
        units: Optional[str] = "metric",
        lang: Optional[str] = "pt_br"
    ) -> dict:

        forecast = weather_cache.get_weather(city, state, country, units)
        if forecast:
            return forecast

        openweather_connector = OpenWeatherConnector(
            city=city, state=state, country=country, units=units, lang=lang)
        report = await openweather_connector.send_async()
        report = report.json()
        report_main = report["main"]

        weather_cache.set_weather(city, state, country, units, report_main)
        return report_main
