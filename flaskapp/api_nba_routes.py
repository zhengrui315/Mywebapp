from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify

from flaskapp.model.utils import create_mysql_engine
from flaskapp.model.nba import Game, Team
from sqlalchemy.orm import sessionmaker

nba_bp = Blueprint('api_nba_bp', __name__, url_prefix='/api/nba/')


@nba_bp.route('/arena/', methods=['GET'])
def get_arena_list():

    engine = create_mysql_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        data = session.query(Team).all()
        arena_list = []

        for row in data:
            arena = dict()
            arena['team_name'] = row.team_name
            arena['arena_name'] = row.arena_name
            arena['latitude'] = row.latitude
            arena['longitude'] = row.longitude
            arena_list.append(arena)

        return jsonify({'arena_list':arena_list}), 200
    except Exception as e:
        print(str(e))
        raise e
    finally:
        session.close()

