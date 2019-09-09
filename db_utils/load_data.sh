#!/bin/bash

python travelers_project/manage.py flush
python travelers_project/manage.py makemigrations
python travelers_project/manage.py migrate

cd travelers_project
python manage.py loaddata geography/fixtures/region.json
python manage.py loaddata geography/fixtures/type_of_sights.json
python manage.py loaddata geography/fixtures/city.json
python manage.py loaddata geography/fixtures/sight.json
python manage.py loaddata geography/fixtures/section_of_sights.json
python manage.py loaddata geography/fixtures/sight_photo.json
