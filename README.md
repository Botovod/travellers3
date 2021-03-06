# travellers3

GraphQL: 
127.0.0.1:8000/graphql/
запрос списка городов в маршруте (маршрут определяется по id или по названию)
~~~
{
  citiesInTrace(id: 2) {
    city {
      title
      rating
    }
  }
}
~~~

запрос списка маршрутов по городам
~~~
{
  cityTraces {
    id
    title
    cities {
      title
    }
  }
}
~~~

запрос списка фотографий достопримечательностей с максимальным рейтином в регионе (по id региона)
~~~
{
  bestSightphotoInRegion(id: 129) {
    id
    title
    file
  }
}
~~~

запрос списка достопримечательностей с максимальным рейтином в регионе (по id региона)
~~~
{
  bestSightInRegion(id: 129){
    id
    title
    rating
  }
}
~~~

запрос списка городов с максимальным рейтином в регионе (по id региона)
~~~
{
  bestCities(region_id: 143){
    title
    rating
  }
}
~~~

запрос информации о регионе по названию:
~~~
{
  region(title: "Воронежская область") {
    id
    title
    description
    city {
      id
      title
      rating
      sight {
        id
        title
      }
    }
  }
}
~~~

запрос списка городов в базе:
~~~
{
  allCities {
    title
    id
    description
    sight{
      id
      title
    }
  }
}
~~~


Для загрузки тестовых данных в терминале перейти в корневой каталог и выполнить:
~~~
bash db_utils/load_data.sh 
~~~
Установка виртуальной среды:
перейти в корневой каталог и выполнить:
```
virtualenv -p python3.7 ./venv
```
Активировать виртуальную среду:
перейти в корневой каталог и выполнить:
```
source venv/bin/activate
```
Установка зависимостей:
перейти в корневой каталог и выполнить:
```
pip install -r requirements.txt
```
Каталог nginx:
файл default скопировать в каталог /etc/nginx/sites-available/

Каталог supervisor:
файл travelers_project.conf, celery.conf и celery_beat.conf скопировать в каталог /etc/supervisor/conf.d/

Для загрузки изображений из vk необходимо в файле local_settings.py
задать значение полям VK_LOGIN, VK_PASSWORD,
перейти в корневой каталог и выполнить:
```
python manage.py vkloader
```
