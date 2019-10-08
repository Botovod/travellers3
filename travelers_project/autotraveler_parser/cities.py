import asyncio
import aiohttp
import logging
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from autotraveler_parser.connect import connect, connect_for_images
from autotraveler_parser.utils import create_path_for_image
from geography.models import City, Region

logger = logging.getLogger(__name__)

async def cities():

    url = '/towns.php'
    soup = await connect(url)

    list_url = []
    try:
        for div in soup.find_all('div', class_='tblock'):
            for a in div.find_all('a'):
                list_url.append(a.get('href'))
    except AttributeError as e:
        logger.error(e)

    return list_url


def write_image(data, title):
    path_to_image, image = create_path_for_image('cities', title)

    # Запись файла
    with open(path_to_image, 'wb') as file:
        file.write(data)

    return image


async def city(c):

    soup = await connect(c)
    try:
        title = soup.find('ol', class_='breadcrumb').find('h1').text
    except AttributeError as e:
        title = ''
        logger.error(e)

    if title:
        try:
            region = soup.select_one('li:nth-child(2) .travell5n span').text
        except AttributeError as e:
            region = ''
            logger.error(e)

        try:
            # Получить путь до большой картинки
            path_img = soup.find_all('img', class_='sp-image')[1].get('data-image')     # /album/170.jpg
        except (AttributeError, IndexError) as e:
            logger.error(e)
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
            logger.error(e)

        if not desc:
            text = ''
        text = "\n\n".join(list(elem.string for elem in desc if isinstance(elem.string, str)))

        await save_in_db(title, region, image, text)


async def save_in_db(title, region, image, text):

    try:
        region = Region.objects.get(title=region)
    except (MultipleObjectsReturned, ObjectDoesNotExist) as e:
        region = None
        logger.error(e)


    city, status = City.objects.get_or_create(title=title)

    if status:
        city.region = region
        city.image = image
        city.description = text
        city.save()
        print(f"{title} added.......{city.id}")


async def main():

    city_list = await cities()

    tasks = []
    for c in city_list:
        tasks.append(asyncio.create_task(city(c)))

    await asyncio.gather(*tasks)
