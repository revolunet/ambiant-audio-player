# -*- encoding: UTF-8 -*-

import os
import json
import logging
import base64
from bottle import run, route

import config
import utils
from Room import Room

FORMAT = '%(asctime)-15s %(levelname)-6s %(message)s'
logging.basicConfig(format=FORMAT)

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

SUCCESS = {'success': True}
ERROR = {'success': False}

def start():
    log.info('starting player')
    if not os.path.isdir(config.cache_dir):
        os.makedirs(config.cache_dir)
    player_files = utils.init_cache()
    # start pygame
    room = Room(loop_url=player_files.get('loop'))

    @route('/cache')
    def cache():
        ''' list cached sounds '''
        log.info('API:cache')
        def decode(path):
            begin, ext = os.path.splitext(path)
            begin = begin[begin.rfind('/') + 1:]
            return base64.b64decode(begin)
        keys = [decode(key) for key in room.sounds.keys()]

        return json.dumps(keys)

    @route('/sound/<sound_url:path>')
    def sound(sound_url):
        ''' play any sound on this device '''
        log.info('API:sound %s', sound_url)
        room.play_sound(sound_url, lower_loop_volume = True)
        return SUCCESS

    # start bottle server
    log.info('server started')
    run(host='0.0.0.0', port=8080)


if __name__=='__main__':
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    os.chdir(BASE_DIR)
    start()
