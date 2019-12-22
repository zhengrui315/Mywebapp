from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from flaskapp.model.utils import create_mysql_engine

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    description = Column(String(1024))

    def __repr__(self):
        return f'<Item(name={self.name}, description={self.description}>'

# create the table in our db
engine = create_mysql_engine()
Base.metadata.create_all(engine)