from functools import lru_cache
import xml.etree.ElementTree as ET
import aiohttp
import asyncio

API_URL = "http://www.cbr.ru/scripts/XML_daily.asp?date_req={}"


@lru_cache
async def get_rate(session, url, currency_id="R01235", date=None):
    async with session.get(url) as resp:
        response = await resp.text()
        response_xml = ET.fromstring(response)
        currency_node = response_xml.find(f".//*[@ID='{currency_id}']")
        return {date: currency_node.find("Value").text}


async def fetch_rates(dates):

    async with aiohttp.ClientSession() as session:

        tasks = []
        for date in dates:
            url = API_URL.format(date)
            tasks.append(
                asyncio.ensure_future(get_rate(session, url, date=date))
            )

        dates = await asyncio.gather(*tasks)
        dates_dict = {}
        for date in dates:
            dates_dict.update(date)
        # print(f"{dates_dict=}")
        return dates_dict


def fetch_rates_by_date(dates):
    return asyncio.run(fetch_rates(dates))
