#!/usr/bin/env python

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

    logging.basicConfig(format='%(message)s', level=logging.INFO)
    log = logging.getLogger(__name__)

    log.info('Starting process.')
    bucket_io = BucketIO()
    bucket_io.bucket_name = 'cloud-cloud-composer-testing'
    bucket_io.bucket = bucket_io.get_bucket()

    blob = bucket_io.bucket.blob('test_upload')

    blob.upload_from_string(
        ', '.join(bucket_io.get_filenames()),
        content_type='text'
    )

    log.info('Finishing process.')
