from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


MYSQL_DEFAULTS = {
    'HOST': 'db',
    'PORT': 3306,
    'USER': 'root',
    'PASSWORD': 'root',
    'DBNAME': 'mydb'
}


def create_mysql_engine():
    user = MYSQL_DEFAULTS['USER']
    password = MYSQL_DEFAULTS['PASSWORD']
    host = MYSQL_DEFAULTS['HOST']
    port = MYSQL_DEFAULTS['PORT']
    dbname = MYSQL_DEFAULTS['DBNAME']

    uri = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{dbname}'

    return create_engine(uri)
