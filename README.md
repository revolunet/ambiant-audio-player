
# ambiantplayer

Audio player for in-stores sound-system that offers a simple HTTP API to play on-demand sounds.

It can play an infinite sound loop in background and play on-demand sounds via HTTP API.

It use [pygame](http://pygame.org) and in-memory sounds to be extra-reactive, even on small devices like [raspberry PI](https://www.raspberrypi.org/).

 - Play local/remote OGG files on-demand
 - Play a background sound loop
 - Expose sound control HTTP API on http://0.0.0.0:8080
 - Sounds cache management

## Setup

`pip install git+https://github.com/revolunet/ambiantplayer.git`

edit [config.py](./config.py.sample) and run `python -m ambiantplayer`

## Usage

Just run `python -m ambiantplayer`.
It will read config from `config.py`.

### Preload config (optional)

If you specify a local path or url in `config.cache_preload_url`, the player expects to find this JSON and it will cache & preload files defined there.

```json
{
    "loop": "http://sounds.com/store-1/loop.ogg",
    "sounds": [
        "http://sounds.com/store-1/welcome.ogg",
        "http://sounds.com/store-1/closing.ogg",
        "http://sounds.com/store-1/warning.ogg"
    ]
}
```

### HTTP API

 - **GET `/cache`** : list cached files
 - **GET `/play/http://sounds.com/example.ogg`** : play and cache the sound at that url


### Notes on OSX

I had to install a 32bit python version to make pygame work for some reason.
So from OSX i start it with `python2-32 player.py`

### Todo
 - auto-start script
 - IPE-RO/RW support and soft failure on error
 - support other file types
