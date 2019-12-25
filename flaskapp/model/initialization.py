# one-time run to initialize the database
# it should be ran inside flask container:
# (1) enter the container by: docker exec -it mywebapp_flask /bin/bash
# (2) under the root directory of the repo, run: python -m flaskapp.model.initialization
# the alternative is to create a .sql file and add it to docker-compose.yml file: "- ./dump.sql:/docker-entrypoint-initdb.d/dump.sql:ro"
# this sql file can be obtained using "mysqldump" command


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

if __name__ == '__main__':
    initialize()


