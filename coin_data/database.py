def get_database_dict():
    return {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'myprojectdb',
            'USER': 'myprojectuser',
            'PASSWORD': 'PasswordDB.123',
            'HOST': 'localhost',
            'PORT': '',
        }
    }