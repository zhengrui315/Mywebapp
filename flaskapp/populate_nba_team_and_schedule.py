from flaskapp.model.utils import create_mysql_engine
from flaskapp.model.nba import Team, Game

from sqlalchemy.orm import sessionmaker
import json
import os
import datetime


def populate_team(filename):
    engine = create_mysql_engine()
    Session = sessionmaker(bind=engine)

    session = Session()
    try:
        if len(session.query(Team).all()) > 0:
            return

        with open(filename, 'r') as f:
            team_data = json.load(f)

        for k, v in team_data.items():
            team = Team(team_name=k,
                        division=v['division'],
                        arena_name=v['arena_name'],
                        address=v['address'],
                        latitude=v['latitude'],
                        longitude=v['longitude'])
            session.add(team)
        session.commit()
    except Exception as e:
        print(e)
        raise e
    finally:
        session.close()


def fetch_team_id(session):
    name_id = dict()
    for i, name in session.query(Team.id, Team.team_name):
        name_id[name] = i
    return name_id


def time_12_24(s):
    """ the input time string s is the form 'hh:mm am ET', convert into 24h format """
    assert len(s.split()) == 3, 'The time format is wrong'
    s1, s2, s3 = s.split()
    h, m = map(int, s1.split(':'))
    assert s3 == 'ET', 'Found an exception with timezone'

    if h == 12:
        h = 0

    if s2.lower() == 'am':
        return h, m
    elif s2.lower() == 'pm':
        return h + 12, m


def populate_game(filename):
    engine = create_mysql_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        name_id = fetch_team_id(session)
        with open(filename, 'r') as f:
            game_data = json.load(f)

        for k, v in game_data.items():
            # date:
            y, m, d = map(int, k.split('-'))
            game_date = datetime.date(year=y, month=m, day=d)

            for g in v:
                # time:
                h, m = time_12_24(g[0])
                game_time = datetime.time(hour=h, minute=m)

                game = Game(
                    home_id=name_id[g[2]],
                    away_id=name_id[g[1]],
                    date=game_date,
                    time=game_time
                )
                session.add(game)
        session.commit()
    except Exception as e:
        print(e)
        raise e
    finally:
        session.close()


if __name__ == '__main__':
    path = './webcrawler/nba/nbadata'

    team_json = os.path.join(path, 'team_full.json')
    populate_team(team_json)

    for month in ['jan', 'feb', 'mar', 'apr']:
        game_json = os.path.join(path, f'schedule_{month}.json')
        populate_game(game_json)

