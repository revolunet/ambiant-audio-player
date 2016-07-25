# -*- encoding: UTF-8 -*-

import os
import json
import logging
import base64
from bottle import run, route, static_file
import timeit

import config
import utils
from Room import Room

FORMAT = '%(asctime)-15s %(levelname)-6s %(module)-8s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

SUCCESS = {'success': True}
ERROR = {'success': False}


class Timer(object):
    def __init__(self, title):
        self.title = title
    def __enter__(self):
        self.start_time = timeit.default_timer()
        return self
    def __exit__(self, *args):
        elapsed = timeit.default_timer() - self.start_time
        logging.info('%s duration : %ss', self.title, elapsed)



def start():
    logging.info('starting player')
    if not os.path.isdir(config.cache_dir):
        os.makedirs(config.cache_dir)

    with Timer('init_cache') as t:
        player_files = utils.init_cache()

    # start pygame
    with Timer('Room.init') as t:
        room = Room(loop_url=player_files.get('loop'))

    @route('/cache')
    def cache():
        ''' list cached sounds '''
        logging.info('API:cache')
        def decode(path):
            begin, ext = os.path.splitext(path)
            begin = begin[begin.rfind('/') + 1:]
            return base64.b64decode(begin)
        keys = [decode(key) for key in room.sounds.keys()]

        return json.dumps(keys)

    @route('/play/<sound_url:path>')
    def play(sound_url):
        ''' play any sound on this device '''
        logging.info('API:sound %s', sound_url)
        room.play_sound(sound_url, lower_loop_volume = True)
        # return empty pixel to satisify browsers using image.src
        # todo: return response when application/json header
        return static_file('pixel.gif', '.')

    # start bottle server
    logging.info('server started')
    run(host='0.0.0.0', port=8080)


if __name__=='__main__':
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    os.chdir(BASE_DIR)
    start()
