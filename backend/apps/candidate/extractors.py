import os
import string

import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings
from decouple import config

CV_URL = config('CV_URL', default=string.ascii_letters)


def extract(file):
    path = default_storage.save('./tmp/'+file.name, ContentFile(file.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)
    files = [
        ('cv', (file.name, open(tmp_file, 'rb'), 'application/pdf'))
    ]
    response = requests.request("POST", CV_URL, files=files)
    os.remove(tmp_file)
    return response.json()