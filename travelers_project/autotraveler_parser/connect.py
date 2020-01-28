from bs4 import BeautifulSoup as bs
import logging
import asyncio
import aiohttp


async def connect(url):
    base_url = 'http://autotravel.ru'

    while True:
        try:
            async with aiohttp.ClientSession() as session:
                while True:
                    async with session.get(base_url + url, ssl=False) as response:
                        if response.status != 503:
                            soup = bs(await response.text(), "html.parser")
                            return soup
                        else:
                            await asyncio.sleep(2)

        except Exception as e:
            continue


async def connect_for_images(url):
    base_url = 'http://autotravel.ru'

    while True:
        try:
            async with aiohttp.ClientSession() as session:
                while True:
                    async with session.get(base_url + url, ssl=False) as response:
                        if response.status != 503:
                            data = await response.read()
                            return data
                        else:
                            await asyncio.sleep(2)
        except Exception as e:
            continue
