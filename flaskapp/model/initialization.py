# one-time run to initialize the database

from flaskapp.model.utils import create_mysql_engine
from flaskapp.model.models import Item
from sqlalchemy.orm import sessionmaker

def initialize():
    engine = create_mysql_engine()
    Session = sessionmaker(bind=engine)

    session = Session()
    try:
        item1 = session.query(Item).filter_by(name='item1').first()
        if not item1:

            item1 = Item(name='item1', description='sample description')
            session.add(item1)
            session.commit()
    except Exception as e:
        print(e)
        raise e
    finally:
        session.close()


