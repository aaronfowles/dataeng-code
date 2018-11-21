#!/usr/bin/env python

import logging

if __name__ == '__main__':

    logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    log.info('Starting process.')

    log.info('Finishing process.')
