from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


MYSQL_DEFAULTS = {
    'HOST': 'db',
    'PORT': 3306,
    'USER': 'root',
    'PASSWORD': 'root',
    'DBNAME': 'mydb'
}

MYSQL_HOST = {
    'HOST': 'localhost',
    'PORT': 32000,
    'USER': 'root',
    'PASSWORD': 'root',
    'DBNAME': 'mydb'
}


def create_mysql_engine():
    params = MYSQL_DEFAULTS
    user = params['USER']
    password = params['PASSWORD']
    host = params['HOST']
    port = params['PORT']
    dbname = params['DBNAME']

    uri = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{dbname}'

    return create_engine(uri)
