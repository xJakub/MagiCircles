from django.utils.translation import ugettext_lazy as _

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '%no*6sl#g&34vg61&4zs*pjk+gb9_ma-oua!@h1o0wn3fxb!k#'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'magi/locale'),
]

SITE = 'none'
AWS_SES_RETURN_PATH = 'none@no.ne'
STATIC_UPLOADED_FILES_PREFIX = ''

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
    ('ru', _('Russian')),
    ('it', _('Italian')),
    ('fr', _('French')),
    ('de', _('German')),
    ('pl', _('Polish')),
    ('ja', _('Japanese')),
    ('kr', _('Korean')),
    ('zh-hans', _('Simplified Chinese')),
    ('pt-br', _('Brazilian Portuguese')),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
            ],
        },
    },
]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'magi',
)

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
)
