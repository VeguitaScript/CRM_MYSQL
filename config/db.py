import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SQLITE={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

# MYSQL = {
#   'default':{
#   'ENGINE':'django.db.backends.mysql',
#   'NAME':os.environ.get('DBNAME'),
#   'USER':os.environ.get('DBUSER'),
#   'PASSWORD':os.environ.get('DBPASS'),
#   'HOST':os.environ.get('DBHOST'),
#   'PORT':'3308'
#   }
# }

MYSQL = {
  'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '',
        'NAME': 'crm_mysql',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}



