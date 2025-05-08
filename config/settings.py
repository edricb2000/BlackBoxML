"""
Django settings for the core project.

Located at: Project/core/settings.py

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

import os
from pathlib import Path
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR should point to the project root directory (Project/)
# which is three levels up from this settings file (settings.py -> settings -> core -> Project)
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s(q19uf6ey4w$w9(s*smqb#dn95yc9i#@-n-x!%9abr95_pi(r' # CHANGE THIS IN PRODUCTION!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # Set to False in production

ALLOWED_HOSTS = ['165.232.154.148', '127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Your apps (ensure these directories exist directly under BASE_DIR, i.e., /app/frontend, /app/backend, /app/core)
    'frontend.apps.FrontendConfig',
    'backend.apps.BackendConfig', # Assuming you have a 'backend' app like 'frontend'
    'core.apps.CoreConfig',       # Assuming 'core' is also a Django app located at /app/core
    # Third-party apps
    'stripe', # Assuming you have 'django-stripe' or similar installed via requirements.txt
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SECURE = True  # Only send CSRF cookie over HTTPS
SESSION_COOKIE_SECURE = True  # Only send session cookie over HTTPS

# Point to the urls.py file in the 'core' app directory
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Looks for templates in /app/core/templates/
        'DIRS': [BASE_DIR / 'core' / 'templates'],
        # APP_DIRS = True is usually recommended to automatically find templates
        # inside each app's 'templates' directory (e.g., /app/frontend/templates/).
        # Setting it to False means you *must* define all template locations in 'DIRS'.
        # Consider changing this to True if your apps have their own template folders.
        'APP_DIRS': False, # Change to True? See comment above.
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 'builtins': [], # Usually not needed unless adding custom template tags globally
        },
    },
]

# Use the wsgi.py file located in /app/core/wsgi.py
WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# Database file will be located at /app/db.sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True # Recommended for handling timezones correctly


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# URL to use when referring to static files located in STATIC_ROOT
STATIC_URL = '/static/'

# Directory where `collectstatic` will gather static files for deployment.
# Will be located at /app/staticfiles/
# You generally don't serve from this in development with DEBUG=True.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Additional locations the staticfiles app will traverse to find static files.
# Looks for static files in /app/core/static/
STATICFILES_DIRS = [
    BASE_DIR / 'core' / 'static',
    # If your other apps have static files NOT in an app-specific 'static' subdir,
    # add them here, e.g.:
    # BASE_DIR / 'frontend' / 'static_custom',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Add any other custom settings below ---
# Example for Stripe (replace with your actual keys)
# --- Add any other custom settings below ---
# Example for Stripe (replace with your actual keys)
STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_SECRET = os.environ.get('STRIPE_WEBHOOK_SECRET')