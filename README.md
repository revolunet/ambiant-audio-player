# httpaudioplayer

Minimal Python audio player for in-stores sonorisation that offers a basic HTTP API to play on-demand sounds.

It can play an infinite sound loop in background and play on-demand sounds via HTTP API.

Based on [pygame](http://pygame.org), works nicely with [raspberry PI](https://www.raspberrypi.org/).

 - Play local/remote OGG files on-demand
 - Play a background sound loop
 - Expose sound control HTTP API on http://0.0.0.0:8080

:bulb: If you're looking for a full-featured, battle-tested music server, go checkout [MOPIDY](https://github.com/mopidy/mopidy)

## Install

 - [download](https://github.com/revolunet/httpaudioplayer/archive/master.zip) the project
 - `pip install -r requirements.txt`

Run with `python player.py /path/to/some/loop.ogg`

## Auto start

 - add `/home/pi/httpaudioplayer/start.sh &` to `/etc/rc.local`
 - use `screen -x` to get the player session

### HTTP API

serves on port 8082

 - **GET `/play/http://sounds.com/example.ogg`** : download and play
 - **GET `/loop/http://sounds.com/example-loop.ogg`** : download and play this sound as loop

### Notes on OSX

I had to install a 32bit python version to make pygame work for some reason.

So from OSX i start it with `python2-32 player.py`

### Todo
 - support other file types
 - caching/pre-heat
