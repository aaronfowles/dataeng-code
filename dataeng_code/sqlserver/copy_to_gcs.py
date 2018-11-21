#!/usr/bin/env python

import logging


def do_something():
    return 'something'


if __name__ == '__main__':

    logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s', level=logging.INFO)
    log = logging.getLogger(__name__)

    log.info('Starting process.')

    log.info('Finishing process.')
