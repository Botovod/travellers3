#!/bin/bash


cd travelers_project

python manage.py loaddata geography/fixtures/region.json
python manage.py loaddata geography/fixtures/city.json
python manage.py loaddata geography/fixtures/typeofsights.json
python manage.py loaddata geography/fixtures/sectionofsights.json
python manage.py loaddata geography/fixtures/sight0.json
python manage.py loaddata geography/fixtures/sight1.json
python manage.py loaddata geography/fixtures/sight2.json
python manage.py loaddata geography/fixtures/sight3.json
python manage.py loaddata geography/fixtures/sight4.json
python manage.py loaddata geography/fixtures/sight5.json
python manage.py loaddata geography/fixtures/sight6.json
python manage.py loaddata geography/fixtures/sightphoto0.json
python manage.py loaddata geography/fixtures/sightphoto1.json
python manage.py loaddata geography/fixtures/sightphoto2.json
