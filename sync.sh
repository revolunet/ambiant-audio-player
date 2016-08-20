#!/bin/sh

FILES="requirements.txt rc.local config.py.sample init-cache.py Room.py player.py utils.py pixel.gif"
DEST_PATH="/home/ju/ambiantplayer/"

function sync() {
  DEST=$1
  ssh $DEST ipe-rw
  rsync -v $FILES $DEST:$DEST_PATH
  ssh $DEST ipe-ro
}

sync $1




