"""from django.conf import settings
from django.backends.s3boto3 import S3Boto3Storages

class StaticFileStorage(S3Boto3Storages):
    location = settings.STATICFILES_FOLDER

class MediaFileStorage(S3Boto3Storages):
    location = settings.MEDIAFILES_FOLDER"""