import logging

from structlog import get_logger, wrap_logger
from structlog.processors import JSONRenderer

if __name__ == '__main__':

    logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    log = wrap_logger(
        logger,
        processors=[
            JSONRenderer(indent=4, sort_keys=True)
        ]
    )
    log.info('Starting process.')

    log.info('Finishing process.')
