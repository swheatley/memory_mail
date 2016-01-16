"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# !!!Remember this has to do with CustomManager and CustomUser!!!!
AUTH_USER_MODEL = 'main.CustomUser'  
SOCIAL_AUTH_USER_MODEL = 'main.CustomUser' 

# Quick-start development settings - unsuitable for production
#  See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '25rv1j5k)3589&hz%dv1_ikys+8bo48vhqh=v7op@i8r3u)-1z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'main',
    'checkout',
    'social.apps.django_app.default',
    'registration',
    'crispy_forms',
    'bootstrap3',
    'stripe',
    'debug_toolbar',


]
SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap3'

ACCOUNT_ACTIVATION_DAYS = 3
REGISTRATION_AUTO_LOGIN = True
# LOGIN_REDIRECT_URL = '/'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    
    'social.backends.twitter.TwitterOAuth',
    'social.backends.google.GoogleOAuth2',
    'social.backends.instagram.InstagramOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.stripe.StripeOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    


 )
# #SOCIAL_AUTH_PIPELINE = (

#     'social.pipeline.social_auth.social_details',
#     'social.pipeline.social_auth.social_uid',
#     'social.pipeline.social_auth.auth_allowed',
#     'social.pipeline.social_auth.social_user',
#     'social.pipeline.user.get_username',
#     'social.pipeline.social_auth.associate_by_email',  # <-- this one does the trick
#     'social.pipeline.user.create_user',
#     'social.pipeline.social_auth.associate_user',
#     'social.pipeline.social_auth.load_extra_data',
#     'social.pipeline.user.user_details'
# )

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.template.context_processors.csrf',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_auth.context_processors.social_auth_by_type_backends',
                # 'social.apps.django_app.context_processors.associated',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],

        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'memory_mail',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'root',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGIN_URL = '/dashboard'
LOGIN_REDIRECT_URL = '/dashboard'

# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/dashboard'
 
# SOCIAL_AUTH_LOGIN_URL = '/dashboard'
# SOCIAL_AUTH_LOGIN_URL = '/'
# SOCIAL_AUTH_INSTAGRAM_REDIRECT_URL = 'http://localhost:8000/complete/instagram'
# working :)
SOCIAL_AUTH_TWITTER_KEY = '9rCc3lx8eN6FmPoGWpDWYBUUM' 
SOCIAL_AUTH_TWITTER_SECRET = 'XkQgkmLTA5TJ6jbuGznBjCA4SZPio1zFo6VqcPVmUGN5JAuF51'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '567871385083-sjhepk7nmquvjlcs8rfergf8hl56v90g.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '8h2HilLXMg_nUp8tHhHjM2Ot'

# not working :(
SOCIAL_AUTH_INSTAGRAM_KEY = '4a0f126f6ec64c929ad658b899d44252'
SOCIAL_AUTH_INSTAGRAM_SECRET = '1296c9b298d5492dad2a53f12e5d0f07'

# AIzaSyD8c4MtQrNeoU5I-yeW6KvI9b5W3I5_uRI
SOCIAL_AUTH_FACEBOOK_KEY = '931246330263182'
SOCIAL_AUTH_FACEBOOK_SECRET = '88808c535bbba633e6205089fb5e31f4'

# FACEBOOK_EXTENDED_PERMISSIONS = ['email']
  



# Stripe Stuff

# test keys
STRIPE_PUBLIC_KEY = 'pk_test_abDKoFj8mdk1c2LkW1R21T7k'
STRIPE_SECRET_KEY = 'sk_test_VvkPjFcKvIHib7Yy13ZNdWRi'


# # live keys
# STRIPE_PUBLISHABLE_KEY = ''
# STRIPE_SECRET_KEY = ''
