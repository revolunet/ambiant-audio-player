# -*- encoding: UTF-8 -*-

import utils
import logging

FORMAT = '%(asctime)-15s %(levelname)-6s %(module)-8s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

utils.init_cache()