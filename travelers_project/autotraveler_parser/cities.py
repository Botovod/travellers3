import asyncio
import aiohttp
import logging
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from autotraveler_parser.connect import connect, connect_for_images
from autotraveler_parser.utils import create_path_for_image
from autotraveler_parser.sights import get_all_sights_by_city, parse_sight
from geography.models import City, Region

logger = logging.getLogger(__name__)


async def parse_pages_with_cities():
    url = "/towns.php"
    soup = await connect(url)
    list_url = []
    
    try:
        for div in soup.find_all('div', class_='col-xs-12 well'):
            for a in div.find_all('a', class_='travell5m'):
                list_url.append(a.get('href'))
    except AttributeError as e:
        logger.error(f'{e}......{url}')

    return list_url
            

async def parse_cities(list_with_pages_urls):
    list_url = []

    for url in list_with_pages_urls:
        soup = await connect(url)

        try:
            for a in soup.find('div', class_='column').find_all('a', {'class': ['travell5m', 'travell9b']}):
                list_url.append(a.get('href'))
        except AttributeError as e:
            logger.error(f'{e}......{url}')

    return list_url


def write_image(data, title):
    path_to_image, image = create_path_for_image('cities', title)

    # Запись файла
    with open(path_to_image, 'wb') as file:
        file.write(data)

    return image


async def parse_city(c):
    soup = await connect(c)
    try:
        title = soup.find('ol', class_='breadcrumb').find('h1').text
    except AttributeError as e:
        title = ''
        logger.error(f'{e}......title {c}')

    if title:
        try:
            region = soup.select_one('li:nth-child(2) .travell5n span').text
        except AttributeError as e:
            region = ''
            logger.error(f'{e}......region')

        try:
            # Получить путь до большой картинки
            path_img = soup.find_all('img', class_='sp-image')[1].get('data-image')     # /album/170.jpg
        except (AttributeError, IndexError) as e:
            logger.error(f'{e}......sp-image')
            path_img = ''

        if path_img:
            # Конектится по полученному пути и получить фаил с бинарными данными картинки
            data = await connect_for_images(path_img)
            # Записать их в media/images/...
            image = write_image(data, title)
        else:
            image = ''

        try:
            desc = soup.find('div', class_='col-xs-12 well tj t0').contents
        except AttributeError as e:
            desc = ''
            logger.error(f'{e}......description')

        if not desc:
            text = ''
        text = "\n\n".join(list(elem.string for elem in desc if isinstance(elem.string, str)))

        try:
            sights_url = soup.find('h4', class_="text-uppercase").find('a').get('href')
        except AttributeError as e:
            sights_url = ''
            logger.error(f'{e}......sights_url')

        await save_in_db(title, region, image, text)

        res = await get_all_sights_by_city(sights_url)

        await parse_sight(res)


async def save_in_db(title, region, image, text):
    try:
        region, _ = Region.objects.get_or_create(title=region)
    except (MultipleObjectsReturned, ObjectDoesNotExist) as e:
        region = ''
        logger.error(f'{e}......region in db')

    city, status = City.objects.get_or_create(title=title)

    if status:
        if region:
            city.region = region
        if image:
            city.image = image
        if text:
            city.description = text
        city.save()
        print(f"{title} added.......{city.id}")


async def main():
    pages_list = await parse_pages_with_cities()
    city_list = await parse_cities(pages_list)
    urls = []
    tasks = []
    for c in city_list:
        tasks.append(asyncio.create_task(parse_city(c)))
        # urls.append(await parse_city(c))

    await asyncio.gather(*tasks)

    return urls
