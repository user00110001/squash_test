import os
import logging

log = logging.getLogger(__name__)


if __name__ == '__main__':
    logging.basicConfig()
    log = logging.getLogger('king')
    log.info('I am still the king of the world!')
