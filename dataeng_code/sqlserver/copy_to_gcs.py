#!/usr/bin/env python
import argparse
from google.cloud import storage

import logging

class BucketIO:

    def __init__(self):
        self.bucket_name = None
        self.bucket = None

    def get_bucket(self):
        if self.bucket is None:
            storage_client = storage.Client()
            bucket = storage_client.get_bucket(self.bucket_name)
        else:
            bucket = self.bucket
        return bucket


    def get_filenames(self):
        return [blob.name for blob in self.bucket.list_blobs()]


if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('--ts')

    args = arg_parser.parse_args()

    ts = args.ts

    logging.basicConfig(format='%(message)s', level=logging.INFO)
    log = logging.getLogger(__name__)

    log.info('Starting process.')
    bucket_io = BucketIO()
    bucket_io.bucket_name = 'dev-cloud-composer-testing'
    bucket_io.bucket = bucket_io.get_bucket()

    blob = bucket_io.bucket.blob('{0}-{1}'.format('test', ts)

    blob.upload_from_string(
        '{0}-{1}'.format(', '.join(bucket_io.get_filenames()), ts),
        content_type='text/plain'
    )

    log.info('Finishing process.')
