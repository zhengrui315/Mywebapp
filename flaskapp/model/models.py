from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

from flaskapp.model.utils import create_mysql_engine

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    description = Column(String(1024))

    def __repr__(self):
        return f'<Item(name={self.name}, description={self.description})>'


class CampSite(Base):
    __tablename__ = 'campsites'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    description = Column(String(1024))
    url = Column(String(512))

    def __repr(self):
        return f'<CampSite(name={self.name})>'

###  sample MySQL query for inserting into CampSite:
###  insert into campsites (name, latitude, longitude) values ('test1', 30.347, -97.75), ('test2', 30.0, -98.0);

# create the table in our db
engine = create_mysql_engine()
Base.metadata.create_all(engine)