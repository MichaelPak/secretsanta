#!/bin/sh
pipenv run loaddb
FLASK_APP=manage.py pipenv run server