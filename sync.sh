#!/bin/sh

cd `dirname "$0"`

FILES="requirements.txt player.py start.sh pixel.gif"
DEST_PATH="/root/simpleplayer/"

function sync() {
  TARGET=$1
  ssh $TARGET ipe-rw
  rsync -v $FILES $TARGET:$DEST_PATH
  scp rc.local $TARGET:/etc/rc.local
  ssh $TARGET ipe-ro
}

sync $1




