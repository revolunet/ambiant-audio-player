#!/bin/sh

cd `dirname "$0"`

IP=`ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'`

URL="http://192.168.10.10:9500/getloop?ip=$IP"

echo "GETTING LOOP FROM $URL"

screen -AdmS player -t home
screen -S player -X screen -t init sh -c 'python player.py $URL ; exec bash'
