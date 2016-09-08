

"""
Django settings for testerapi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import allauth
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p^ub5@m$2gg%f8gnhyh45yo8d%m=h7*&-4+sy^$*9cubuvildq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =  True

SITE_ID = 1
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

TEMPLATE_DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_TEM = os.path.join(os.path.join(PROJECT_DIR,'static'),'templates')
TEMPLATE_DIRS = (PROJECT_TEM, 'templates')

ALLOWED_HOSTS = ['localhost', '.herokuapp.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'results',
    'storages',
    'django.contrib.humanize',
    #'debug_toolbar',
    'django.contrib.sites',
    'tastypie',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.instagram',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
# 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ()
# print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
ROOT_URLCONF = 'testerapi.urls'

WSGI_APPLICATION = 'testerapi.wsgi.application'




import dj_database_url


DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
# not the same database as live version

'default': dj_database_url.config(default='postgres://uocqetwjikrvap:v-R2EPrZQstDpmiPEiRl9g6wQw@ec2-54-243-249-65.compute-1.amazonaws.com:5432/d924s0dvs7upd4')

}




LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


#   STATIC_ROOT = "/Users/kevinwojton/Hack/hubheroku/hub3/hub3"

STATIC_ROOT = os.path.join(BASE_DIR,'static')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MEDIA_ROOT = '/home/vagrant/static/media/'
MEDIA_URL = '/media/'


# turn on for real production

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'hubbucketbb'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'



#DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#STATIC_URL = '/static/'

STATIC_URL = 'http://hubbucketbb.s3.amazonaws.com/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'



DEFAULT_FILE_STORAGE = 'testerapi.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'testerapi.s3utils.StaticRootS3BotoStorage'
AWS_QUERYSTRING_AUTH = False


#AWS_ACCESS_KEY_ID = os.environ['AKIAIYZQNIBU4JXZFYZA']
#AWS_SECRET_ACCESS_KEY = os.environ['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']
#AWS_STORAGE_BUCKET_NAME = os.environ['hubbucketaa']

#AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']

#AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

#AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

MEDIA_URL = 'http://%s.s3.amazonaws.com/your-folder/' % AWS_STORAGE_BUCKET_NAME
#DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))


STATIC_URL = '/static/'


STATICFILES_DIRS = (
    'staticfiles',
)
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True
COMPRESS_URL = 'http://testerapibucket.s3.amazonaws.com/'
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_STORAGE = 'storage.CachedS3BotoStorage'

EMAIL_USE_TLS = True

TEMPLATE_CONTEXT_PROCESSORS = (

    # Required by `allauth` template tags
    'django.core.context_processors.request',

)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Already defined Django-related contexts here

                # `allauth` needs this from django
                'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                # 'allauth.account.context_processors.account',
                # 'allauth.socialaccount.context_processors.socialaccount',
            ],


        },
    },
]



AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

)





EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kevin@samizdatcollective.com'  # username of one of my user on the first server
EMAIL_HOST_PASSWORD = 'Skate123'
# EMAIL_PORT = 25
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# ACCOUNT_ADAPTER = 'project.users.allauth.AccountAdapter'
