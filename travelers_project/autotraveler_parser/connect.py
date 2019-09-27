import asyncio
import aiohttp

async def connect(url, semaphore):
    base_url = 'http://autotravel.ru'

    async with aiohttp.ClientSession() as session:
        async with semaphore:
            async with session.get(base_url + url, ssl=False) as response:
                if response.status == 200:
                    return await response.text()
