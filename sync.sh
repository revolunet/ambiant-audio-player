#!/bin/sh

cd `dirname "$0"`

FILES="requirements.txt player.py start.sh pixel.gif"

sync_rpi() {
  TARGET=$1
  DEST_PATH="/root/simpleplayer/"
  ssh $TARGET ipe-rw
  rsync -v $FILES $TARGET:$DEST_PATH
  #scp rc.local $TARGET:/etc/rc.local
  ssh $TARGET pip install cherrypy
  ssh $TARGET ipe-ro
  ssh $TARGET reboot
}


sync_ubuntu() {
  TARGET=$1
  DEST_PATH="/home/ju/simpleplayer"
  rsync -v $FILES $TARGET:$DEST_PATH
 # ssh $TARGET pip install cherrypy
 # ssh $TARGET sudo reboot
}

sync_rpi $1




