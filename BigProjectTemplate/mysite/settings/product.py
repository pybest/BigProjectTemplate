from .base import *


DEBUG = False

ALLOWED_HOSTS = ['210.121.100.37']

# remote MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
