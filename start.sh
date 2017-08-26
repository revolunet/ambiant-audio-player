#!/bin/sh

cd `dirname "$0"`

HOSTNAME=`hostname`

URL="http://192.168.10.10:9500/getloop?hostname=$HOSTNAME"

echo "GETTING LOOP FROM $URL"

screen -AdmS player -t home
screen -S player -X screen -t init sh -c 'python player.py $URL ; exec bash'
