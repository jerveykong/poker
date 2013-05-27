#!/bin/sh

IP="172.16.78.135:8000"
if [ ! -z "$1" ];
    then
        IP=$1
fi

python manage.py runserver $IP
