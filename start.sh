#!/bin/sh

cd `dirname "$0"`

HOSTNAME=`hostname`

URL="http://192.168.0.10:9500/getloop?hostname=$HOSTNAME"

echo "GETTING LOOP FROM $URL"

while true; do
  python ./player.py $URL
  sleep 5
done;
