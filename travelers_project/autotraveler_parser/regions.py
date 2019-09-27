import asyncio
import aiohttp
from bs4 import BeautifulSoup
from geography.models import Region
from autotraveler_parser.connect import connect


async def regions(semaphore):

    response = await connect('/areas.php', semaphore)

    soup = BeautifulSoup(response, 'html.parser')

    links = []
    for block in soup.find_all('div', class_='tblock'):
        for link in block.find_all('a'):
            links.append(link.get('href'))
    return links


async def region(url, semaphore):

    response = await connect(url, semaphore)
    soup = BeautifulSoup(response, 'html.parser')

    try:
        title = soup.find('ul', class_='breadcrumb').find('h1').text
    except:
        pass

    await save_in_db(title)


async def save_in_db(title):

    title = Region.objects.get_or_create(title=title)
    print(f"{title} region is save!")
