from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
import requests
from bs4 import BeautifulSoup as bs

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


@api_bp.route('/campsite/add/', methods=['POST'])
def add_campsite():
    data = request.get_json()
    engine = create_mysql_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        new_campsite = CampSite(name=data['name'],
                                latitude=float(data['latitude']),
                                longitude=float(data['longitude']),
                                description=data['description'])
        session.add(new_campsite)
        session.commit()
        return jsonify({'success':True, 'data':data})
    except Exception as e:
        print(e)
        raise e
    finally:
        session.close()


@api_bp.route('/weather/', methods=['GET'])
def get_weather():
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    url = f'https://forecast.weather.gov/MapClick.php?lat={lat}&lon={lng}'
    response = requests.get(url)
    html = bs(response.content, 'html.parser')

    temp = {}
    summary = html.find(id='current_conditions-summary')
    tempF = summary.find('p', class_='myforecast-current-lrg').get_text()
    tempC = summary.find('p', class_='myforecast-current-sm').get_text()
    temp['tempF'] = tempF.strip()
    temp['tempC'] = tempC.strip()

    weather = {}
    detail = html.find(id='current_conditions_detail')
    details = detail.find_all('tr')
    for row in details:
        cols = row.find_all('td')
        key = cols[0].get_text()
        value = cols[1].get_text()
        weather[key] = value.strip()

    return jsonify({'temp': temp, 'weather': weather})

