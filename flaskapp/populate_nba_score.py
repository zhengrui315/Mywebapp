from flaskapp.model.utils import create_mysql_engine
from flaskapp.model.nba import Team, Game

from sqlalchemy.orm import sessionmaker
import json
import datetime



def fetch_team_id(session):
    name_id = dict()
    for i, name in session.query(Team.id, Team.team_name):
        name_id[name] = i
    return name_id


def populate_score(filename):
    engine = create_mysql_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        name_id = fetch_team_id(session)
        with open(filename, 'r') as f:
            game_score = json.load(f)

        for k, v in game_score.items():
            # date:
            y, m, d = map(int, k.split('-'))
            game_date = datetime.date(year=y, month=m, day=d)

            for g in v:
                away_team, home_team, away_score, home_score = g
                away_id, home_id = name_id[away_team], name_id[home_team]
                game = session.query(Game).filter_by(home_id=home_id, away_id=away_id, date=game_date).first() # .first() doesn't raise exception if doesn't exist
                if not game:
                    game = Game(
                        home_id=home_id,
                        away_id=away_id,
                        date=game_date,
                        home_score=home_score,
                        away_score=away_score
                    )
                    session.add(game)
                else:
                    game.home_score = home_score
                    game.away_score = away_score
        session.commit()
    except Exception as e:
        print(e)
        raise e
    finally:
        session.close()


if __name__ == '__main__':
    filename = './webcrawler/nba/nbadata/score.json'
    populate_score(filename)

