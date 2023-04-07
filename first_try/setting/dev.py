from first_try.settings import *

SECRET_KEY = 'django-insecure-z!!(j__l4^of&#hu(s+)=ocax$&rb-fai4ciww#tlt*5#^n17_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [] 

# SITE_ID = 2
# INSTALLED_APPS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


X_FRAME_OPTIONS= 'SAMEORIGIN'