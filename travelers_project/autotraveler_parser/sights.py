import re
import asyncio
import aiohttp
import logging
from autotraveler_parser.connect import connect, connect_for_images
from autotraveler_parser.utils import create_path_for_image
from geography.models import City, Region, Sight, SightPhoto

# '/otklik.php/1'

logger = logging.getLogger(__name__)

def write_image(data, title):
    path_to_image, image = create_path_for_image('sights', title)
    # Запись файла
    with open(path_to_image, 'wb') as file:
        file.write(data)

    return image

async def sight(url, s):

    soup = await connect(url)

    try:
        title = soup.find('div', class_='panel-heading').find('h1').text
    except AttributeError as e:
        title = ''
        logger.error(f"{e}, .....{url}.")

    if title:

        try:
            city = soup.find('ol', class_='breadcrumb').select_one('li:nth-child(3)').find('a').text
        except AttributeError as e:
            city = ''
            logger.error(e)

        try:
            desc = soup.find('p', class_="tl").text
        except AttributeError as e:
            desc = ''
            logger.error(e)

        try:
            coordinat = soup.select_one('span.t13').text
            coordinat = re.sub('[)(]', '', coordinat).strip()
        except AttributeError as e:
            logger.error(e)
            coordinat = ''

        img_list = []
        links = []
        try:
            for a in soup.find('div', id='fotoimages').find_all('a', class_='atcbox'):
                links.append(a.get('href'))
                if len(links) >= 10:
                    break
        except AttributeError as e:
            logger.error(e)

        if links:
            for link in links:
                data = await connect_for_images(link)
                image = write_image(data, title)
                img_list.append(image)

        await save_db(title, city, desc, img_list, coordinat)

async def save_db(title, sity, desc, img_list, coordinat):

    if sity:
        city, _ = City.objects.get_or_create(title=sity)

    sight, status = Sight.objects.get_or_create(title=title)
    if status:
        sight.city = city
        sight.text = desc
        sight.original_coordinates = coordinat
        sight.image = img_list[0]
        sight.save()

        for img in img_list:
            image = SightPhoto.objects.create(
                sight=sight,
                file=img
            )
            image.save()

        print(f"Saved {title}")

async def main():

    tasks = []

    for s in range(1, 100):
        task = asyncio.create_task(sight(f'/otklik.php/{s}', s))
        tasks.append(task)

    await asyncio.gather(*tasks)
