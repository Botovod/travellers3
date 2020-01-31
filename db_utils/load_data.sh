#!/bin/bash


cd travelers_project

python manage.py loaddata geography/fixtures/geography.json
python manage.py loaddata geography/fixtures/traces.json
python manage.py loaddata geography/fixtures/mainpage.json
