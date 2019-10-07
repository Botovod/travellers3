import asyncio
import aiohttp
from geography.models import Region
from autotraveler_parser.connect import connect, connect_for_images
from autotraveler_parser.utils import create_path_for_image



async def regions():
    url = "/areas.php"
    soup = await connect(url)

    list_url = []
    for div in soup.find_all('div', class_='travell9c'):
        for a in div.find_all('a'):
            list_url.append(a.get('href'))
    return list_url


def write_image(data, title):
    path_to_image, image = create_path_for_image('regions', title)
    # Запись файла
    with open(path_to_image, 'wb') as file:
        file.write(data)
        
    return image


async def region(r):

    soup = await connect(r)
    title = soup.find('ul', class_='breadcrumb').find('h1').text

    try:
        # Получить путь до большой картинки
        path_img = soup.find_all('img', class_='sp-image')[1].get('data-image')     # /album/170.jpg
        # Конектится по полученному пути и получить фаил с бинарными данными картинки
        data = await connect_for_images(path_img)
        # Записать их в media/images/...

        image = write_image(data, title)
    except Exception as e:
        image = None

    await save_in_db(title, image)


async def save_in_db(title, image):

    title, status = Region.objects.get_or_create(title=title)
    if status:
        region = Region.objects.get(title=title)
        region.image = image
        region.save()
        print(f"{title} added......{region.id}")


async def main():

    region_list = await regions()
    tasks = []
    for r in region_list:
        tasks.append(asyncio.create_task(region(r)))

    await asyncio.gather(*tasks)
