from connectors.openweather_connector import OpenWeatherConnector
from typing import Optional


class LocationService:
    async def get_report_async(
        city: str,
        state: Optional[str] = None,
        country: Optional[str] = "BR",
        unit: Optional[str] = "metric",
        lang: Optional[str] = "pt_br"
    ) -> dict:

        openweather_connector = OpenWeatherConnector(
            city=city, state=state, country=country, unit=unit, lang=lang)
        report = await openweather_connector.send_async()
        report = report.json()
        report_main = report["main"]
        return report_main
