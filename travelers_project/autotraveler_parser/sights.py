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


async def get_all_sights_by_city(url):
    sights_urls = []

    soup = await connect(url)
    try:
        for div in soup.find_all('div', class_='col-md-12 col-xs-12'):
            for h3 in div.find_all('h3'):
                sights_urls.append(h3.find('a').get('href'))
    except AttributeError as e:
        logger.error(f"{e}, title.....{url}.")

    return sights_urls


async def parse_sight(urls):
    for url in urls:
        soup = await connect(url)

        try:
            title = soup.find('div', class_='panel-heading').find('h1').text
        except AttributeError as e:
            title = ''
            logger.error(f"{e}, title.....{url}.")

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
                logger.error(f'{e}......description')

            try:
                coordinat = soup.select_one('span.t13').text
                coordinat = re.sub('[)(]', '', coordinat).strip()
            except AttributeError as e:
                logger.error(f'{e}......coordinat')
                coordinat = ''

            img_list = []
            links = []

            try:
                for a in soup.find('div', id='fotoimages').find_all('a', class_='atcbox'):
                    links.append(a.get('href'))
                    if len(links) >= 10:
                        break
            except AttributeError as e:
                logger.error(f'{e}......fotoimages......')

            if links:
                for link in links:
                    data = await connect_for_images(link)
                    image = write_image(data, title)
                    img_list.append(image)

            await save_in_db(title, city, desc, img_list, coordinat)


async def save_in_db(title, sity, desc, img_list, coordinat):
    if sity:
        city, _ = City.objects.get_or_create(title=sity)
    else:
        city = ''

    sight, status = Sight.objects.get_or_create(title=title)

    if status:
        if city:
            sight.city = city
        if desc:
            sight.text = desc
        if coordinat:
            sight.original_coordinates = coordinat
        if img_list:
            sight.image = img_list[0]

            for img in img_list:
                image = SightPhoto.objects.create(
                    sight=sight,
                    file=img
                )
                image.save()

        sight.save()

        print(f"Saved {title}")


async def main():
    tasks = []
    for s in range(1, 5000):
        task = asyncio.create_task(sight(f'/otklik.php/{s}', s))
        tasks.append(task)

    await asyncio.gather(*tasks)
