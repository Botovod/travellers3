import asyncio
import aiohttp
import logging
from geography.models import Region
from autotraveler_parser.connect import connect, connect_for_images
from autotraveler_parser.utils import create_path_for_image

logger = logging.getLogger(__name__)


async def parse_regions():
    url = "/areas.php"
    soup = await connect(url)

    list_url = []
    try:
        for div in soup.find_all('div', class_='travell9c'):
            for a in div.find_all('a'):
                list_url.append(a.get('href'))
    except AttributeError as e:
        logger.error(e)
        
    return list_url


def write_image(data, title):
    path_to_image, image = create_path_for_image('regions', title)
    # Запись файла
    with open(path_to_image, 'wb') as file:
        file.write(data)

    return image


async def parse_region(r):
    soup = await connect(r)
    try:
        title = soup.find('ul', class_='breadcrumb').find('h1').text
    except AttributeError as e:
        title = ''
        logger.error(e)

    if title:
        try:
            # Получить путь до большой картинки
            path_img = soup.find_all('img', class_='sp-image')[1].get('data-image')     # /album/170.jpg
        except (AttributeError, IndexError) as e:
            path_img = ''
            logger.error(e)

        if path_img:
            # Конектится по полученному пути и получить фаил с бинарными данными картинки
            data = await connect_for_images(path_img)
            # Записать их в media/images/...
            image = write_image(data, title)
        else:
            image = ''

        await save_in_db(title, image)


async def save_in_db(title, image):
    region, status = Region.objects.get_or_create(title=title)

    if status:
        region.image = image
        region.save()
        print(f"{title} added......{region.id}")


async def main():
    region_list = await parse_regions()
    tasks = []
    for r in region_list:
        tasks.append(asyncio.create_task(parse_region(r)))

    await asyncio.gather(*tasks)
