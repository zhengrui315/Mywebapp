from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify

from flaskapp.model.utils import create_mysql_engine
from flaskapp.model.models import CampSite
from sqlalchemy.orm import sessionmaker

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/campsites/', methods=['GET'])
def fetch_campsites():
    engine = create_mysql_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    campsites = []
    try:
        data = session.query(CampSite).all()
        for row in data:
            d = {}
            d['id'] = row.id
            d['name'] = row.name
            d['lat'] = row.latitude
            d['lng'] = row.longitude
            campsites.append(d)
    except Exception as e:
        print(e)
        raise e
    finally:
        session.close()
    return jsonify({'campsites':campsites})
