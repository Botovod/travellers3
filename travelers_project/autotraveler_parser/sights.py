import asyncio
import aiohttp
import logging
from autotraveler_parser.connect import connect, connect_for_images
from autotraveler_parser.utils import create_path_for_image
from geography.models import City, Region, Sight, SightPhoto

# '/otklik.php/1'

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
    except Exception as e:
        logging.info(f"{e}, .....{url}.")

    try:
        city = soup.find('ol', class_='breadcrumb').select_one('li:nth-child(3)').find('a').text
    except:
        city = None

    try:
        desc = soup.find('p', class_="tl").text
    except:
        desc = ''

    img_list = []

    try:
        for a in soup.find('div', id='fotoimages').find_all('a', class_='atcbox'):
            data = await connect_for_images(a.get('href'))
            image = write_image(data, title)
            img_list.append(image)
            if len(img_list) >= 10:
                break
    except:
        pass

    try:
        await save_db(title, city, desc, img_list)
    except:
        pass

async def save_db(title, sity, desc, img_list):

    if sity != None:
        city, _ = City.objects.get_or_create(title=sity)

    sight, status = Sight.objects.get_or_create(title=title)
    if status and city:
        sight.city = city
        sight.text = desc
        sight.image = img_list[0] if len(img_list) else None
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
