"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!29u)(zzcv#$28iuf-s=!e_gk8209#rbk(zg%lyj1_!2_fc^*r'

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
    'django.contrib.staticfiles',

    'tailwind',
    'theme',
    'main', #django app
    'client',
    'django_browser_reload',
]

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'



MEDIA_URL = '/images/'





# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CURRENCIES = [

    ('USD', 'US Dollar'),
    ('EUR', 'Euro'),
    ('GBP', 'British Pound Sterling'),
    ('JPY', 'Japanese Yen'),
    ('CNY', 'Chinese Yuan'),
    ('INR', 'Indian Rupee'),
    ('AUD', 'Australian Dollar'),
    ('CAD', 'Canadian Dollar'),
    ('SGD', 'Singapore Dollar'),
    ('NZD', 'New Zealand Dollar'),
    ('BRL', 'Brazilian Real'),
    ('ZAR', 'South African Rand'),
    ('RUB', 'Russian Ruble'),
    ('MXN', 'Mexican Peso'),
    ('CHF', 'Swiss Franc'),
    ('SEK', 'Swedish Krona'),
    ('NOK', 'Norwegian Krone'),
    ('DKK', 'Danish Krone'),
    ('HKD', 'Hong Kong Dollar'),
    ('KRW', 'South Korean Won'),
    ('TRY', 'Turkish Lira'),
    ('IDR', 'Indonesian Rupiah'),
    ('PHP', 'Philippine Peso'),
    ('THB', 'Thai Baht'),
    ('MYR', 'Malaysian Ringgit'),
    ('HUF', 'Hungarian Forint'),
    ('PLN', 'Polish Złoty'),
    ('CZK', 'Czech Koruna'),
    ('ILS', 'Israeli New Shekel'),
    ('CLP', 'Chilean Peso'),
    ('ARS', 'Argentine Peso'),
    ('EGP', 'Egyptian Pound'),
    ('AED', 'United Arab Emirates Dirham'),
    ('QAR', 'Qatari Riyal'),
    ('SAR', 'Saudi Riyal'),
    ('KWD', 'Kuwaiti Dinar'),
    ('OMR', 'Omani Rial'),
    ('BHD', 'Bahraini Dinar'),
    ('JOD', 'Jordanian Dinar'),
    ('LBP', 'Lebanese Pound'),
    ('ILS', 'Israeli Shekel'),
    ('COP', 'Colombian Peso'),
    ('PEN', 'Peruvian Nuevo Sol'),
    ('CLP', 'Chilean Peso'),
    ('UYU', 'Uruguayan Peso'),
    ('VEF', 'Venezuelan Bolivar'),
    ('CRC', 'Costa Rican Colón'),
    ('MXN', 'Mexican Peso'),
    ('GTQ', 'Guatemalan Quetzal'),
    ('HNL', 'Honduran Lempira'),
    ('NIO', 'Nicaraguan Córdoba'),
    ('SVC', 'Salvadoran Colón'),
    ('BZD', 'Belize Dollar'),
    ('BSD', 'Bahamian Dollar'),
    ('JMD', 'Jamaican Dollar'),
    ('KYD', 'Cayman Islands Dollar'),
    ('TTD', 'Trinidad and Tobago Dollar'),
    ('BBD', 'Barbadian Dollar'),
    ('BMD', 'Bermudian Dollar'),
    ('BND', 'Brunei Dollar'),
    ('FJD', 'Fijian Dollar'),
    ('XCD', 'East Caribbean Dollar'),
    ('AUD', 'Australian Dollar'),
    ('NZD', 'New Zealand Dollar'),
    ('PGK', 'Papua New Guinean Kina'),
    ('TOP', 'Tongan Paʻanga'),
    ('SBD', 'Solomon Islands Dollar'),
    ('WST', 'Samoan Tala'),
    ('VUV', 'Vanuatu Vatu'),
    ('KID', 'Kiribati Dollar'),
    ('TVD', 'Tuvaluan Dollar'),
    ('BTN', 'Bhutanese Ngultrum'),
    ('INR', 'Indian Rupee'),
    ('NPR', 'Nepalese Rupee'),
    ('PKR', 'Pakistani Rupee'),
    ('LKR', 'Sri Lankan Rupee'),
    ('MVR', 'Maldivian Rufiyaa'),
    ('MUR', 'Mauritian Rupee'),
    ('SCR', 'Seychellois Rupee'),
    ('TZS', 'Tanzanian Shilling'),
    ('UGX', 'Ugandan Shilling'),
    ('KES', 'Kenyan Shilling'),
    ('RWF', 'Rwandan Franc'),
    ('BIF', 'Burundian Franc'),
    ('SOS', 'Somali Shilling'),
    ('DJF', 'Djiboutian Franc'),
    ('ETB', 'Ethiopian Birr'),
    ('SDD', 'Sudanese Pound'),
    ('SSP', 'South Sudanese Pound'),
    ('GBP', 'British Pound Sterling'),
    ('IEP', 'Irish Pound'),
    ('GIP', 'Gibraltar Pound'),
    ('IMP', 'Isle of Man Pound'),
    ('JEP', 'Jersey Pound'),
    ('FKP', 'Falkland Islands Pound'),
    ('GGP', 'Guernsey Pound'),
    ('SHB', 'Saint Helena Pound'),
    ('SHP', 'Saint Helena Pound'),
    ('EGP', 'Egyptian Pound'),
    ('SDG', 'Sudanese Pound'),
    ('LYD', 'Libyan Dinar'),
    ('TND', 'Tunisian Dinar'),
    ('DZD', 'Algerian Dinar'),
    ('MAD', 'Moroccan Dirham'),
    ('STD', 'São Tomé and Príncipe Dobra'),
    ('AOA', 'Angolan Kwanza'),
    ('ZMW', 'Zambian Kwacha'),
    ('MWK', 'Malawian Kwacha'),
    ('ZAR', 'South African Rand'),
    ('LSL', 'Lesotho Loti'),
    ('NAD', 'Namibian Dollar'),
    ('SZL', 'Swazi Lilangeni'),
    ('BWP', 'Botswana Pula'),
    ('AED', 'United Arab Emirates Dirham'),
    ('QAR', 'Qatari Riyal'),
    ('OMR', 'Omani Rial'),
    ('SAR', 'Saudi Riyal'),
    ('KWD', 'Kuwaiti Dinar'),
    ('BHD', 'Bahraini Dinar'),
    ('JOD', 'Jordanian Dinar'),
    ('LBP', 'Lebanese Pound'),
    ('ILS', 'Israeli Shekel'),
    ('TRY', 'Turkish Lira'),
    ('AZN', 'Azerbaijani Manat'),
    ('GEL', 'Georgian Lari'),
    ('AMD', 'Armenian Dram'),
    ('KZT', 'Kazakhstani Tenge'),
    ('UZS', 'Uzbekistani Som'),
]
