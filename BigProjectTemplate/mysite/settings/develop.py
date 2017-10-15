from .base import *


DEBUG = True

ALLOWED_HOSTS = ['192.168.56.101', '127.0.0.1', 'localhost']

# local MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
