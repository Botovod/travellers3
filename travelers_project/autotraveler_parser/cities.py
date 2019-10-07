import asyncio
import aiohttp
from autotraveler_parser.connect import connect, connect_for_images
from autotraveler_parser.utils import create_path_for_image
from geography.models import City, Region


async def cities():

    url = '/towns.php'
    soup = await connect(url)

    list_url = []
    for div in soup.find_all('div', class_='tblock'):
        for a in div.find_all('a'):
            list_url.append(a.get('href'))
    return list_url


def write_image(data, title):
    path_to_image, image = create_path_for_image('cities', title)

    # Запись файла
    with open(path_to_image, 'wb') as file:
        file.write(data)

    return image


async def city(c):

    soup = await connect(c)
    title = soup.find('ol', class_='breadcrumb').find('h1').text
    region = soup.select_one('li:nth-child(2) .travell5n span').text

    try:
        # Получить путь до большой картинки
        path_img = soup.find_all('img', class_='sp-image')[1].get('data-image')     # /album/170.jpg
        # Конектится по полученному пути и получить фаил с бинарными данными картинки
        data = await connect_for_images(path_img)
        # Записать их в media/images/...
        image = write_image(data, title)
    except Exception as e:
        image = None

    try:
        desc = soup.find('div', class_='col-xs-12 well tj t0').contents
        text = "\n\n".join(list(elem.string for elem in desc if isinstance(elem.string, str)))
    except:
        text = ''

    await save_in_db(title, region, image, text)


async def save_in_db(title, region, image, text):

    try:
        region = Region.objects.get(title=region)
    except:
        region = None


    title, status = City.objects.get_or_create(title=title)

    if status:
        city = City.objects.get(title=title)
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
