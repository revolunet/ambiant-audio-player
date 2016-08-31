#!/bin/sh

cd `dirname "$0"`

HOSTNAME=`hostname`

URL="http://127.0.0.1:9500/getloop?hostname=$HOSTNAME"

echo "GETTING LOOP FROM $URL"

while true; do
  python ./player.py $URL
  sleep 5
done;