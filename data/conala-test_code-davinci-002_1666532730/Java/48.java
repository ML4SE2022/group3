import pprint
import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)

logging.debug(pprint.pformat(some_dict))