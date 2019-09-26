# travellers3


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
файл travelers_project.conf скопировать в каталог /etc/supervisor/conf.d/

Для создания автоматического поста vk на стене сообщества
перейти в корневой каталог и выполнить:
```
python manage.py poster
```
Для загрузки фотографий
перейти в корневой каталог и выполнить:
```
python manage.py loader
```
