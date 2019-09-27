import asyncio
import aiohttp
from bs4 import BeautifulSoup
from autotraveler_parser.connect import connect
from geography.models import City


async def towns(semaphore):

    response = await connect('/towns.php', semaphore)

    soup = BeautifulSoup(response, 'html.parser')

    links = []
    for block in soup.find_all('div', class_='tblock'):
        for link in block.find_all('a'):
            links.append(link.get('href'))
    return links


async def town(url, semaphore):

    response = await connect(url, semaphore)
    soup = BeautifulSoup(response, 'html.parser')

    try:
        title = soup.find('ol', class_='breadcrumb').find('h1').text
    except:
        pass

    try:
        description = soup.find('div', class_='col-xs-12 well tj t0').text
    except:
        description = ''

    await save_in_db(title, description, path)


async def save_in_db(title, description, path):

    title = City.objects.get_or_create(title=title, description=description, image=path)
    print(f"{title} city is save!")
