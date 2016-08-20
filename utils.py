# -*- encoding: UTF-8 -*-

import os
import base64
import logging
import requests
import shutil
import json
import platform
from uuid import getnode as get_mac

import config


def get_unique_path(string):
    ''' convert a path string into a md5, keeping the original extension '''
    path, ext = os.path.splitext(string)
    return '{0}{1}'.format(
        base64.b64encode(string.encode('utf-8')),
        ext
    )

def get_mac_address():
    ''' return properly formatted MAC address '''
    return ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))

def get_hostname():
    ''' return hostname '''
    return platform.node()

def url_to_local_path(url):
    ''' return local path for a given url '''
    return os.path.join(config.cache_dir, get_unique_path(url))

class ReadOnlyException(Exception):
    pass

def download(url, out_path):
    ''' download and save a binary '''
    if os.access(os.path.dirname(out_path), os.W_OK):
        response = requests.get(url, stream=True)
        with open(out_path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        return out_path
    else:
        raise ReadOnlyException()

def get_player_files(url):
    try:
        if url.startswith('http'):
            r = requests.get('{0}?hostname={1}&mac={2}'.format(url, get_hostname(), get_mac_address()) )
            return r.json()
        elif url:
            return json.load(open(url, 'r'))
    except Exception, e:
        logging.exception('ERROR on get_files_to_cache : %s', e)

    return {
        "loop": None,
        "sounds": []
    }

def cache_urls(urls):
    if not urls:
        logging.warning('No file to cache')
        return
    if isinstance(urls, basestring):
        urls = [urls]
    for url in urls:
        if url:
            destination = url_to_local_path(url)
            if os.path.isfile(destination):
                logging.debug('file %s already cached locally', url)
            else:
                logging.debug('download %s for caching', url)
                try:
                    download(url, destination)
                except ReadOnlyException:
                    logging.error('Download: Skip (r/o FS)')
                except Exception, e:
                    logging.error('cant download %s for caching (%s)', url, e)
                else:
                    logging.debug('downloaded %s successfully', url)

def init_cache():
    player_files = get_player_files(config.cache_preload_url)
    player_files_sounds = player_files.get('sounds', [])
    urls_to_cache = []
    if isinstance(player_files_sounds, list):
        urls_to_cache = [player_files.get('loop')] + player_files.get('sounds', [])
    if not os.path.isdir(config.cache_dir):
        if os.access(os.path.dirname(config.cache_dir), os.W_OK):
            os.makedirs(config.cache_dir)
    cache_urls(urls_to_cache)
    # if os.access(config.cache_dir, os.W_OK):
    #     cache_urls(urls_to_cache)
    # else:
    #     logging.error('START:skip init cache directory (r/o FS)')
    return player_files
