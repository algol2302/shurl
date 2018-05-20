#!/bin/bash
./manage.py makemigrations
./manage.py migrate
./manage.py makemigrations shurlapp
./manage.py migrate
