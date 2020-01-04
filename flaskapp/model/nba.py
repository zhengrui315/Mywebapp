import enum
from sqlalchemy import Column, Integer, String, Float, Enum, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from flaskapp.model.utils import create_mysql_engine

Base = declarative_base()

class Division(enum.Enum):
    atlantic = 'Atlantic'
    central = 'Central'
    southeast = 'Southeast'
    northwest = 'Northwest'
    pacific = 'Pacific'
    southwest = 'Southwest'


class Conference(enum.Enum):
    west = 'West'
    east = 'East'


class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    team_name = Column(String(128), unique=True, nullable=False)
    division = Column(Enum(Division))
    conference = Column(Enum(Conference))
    arena_name = Column(String(128), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    address = Column(String(512))
    home_game = relationship('Game', foreign_keys='Game.home_id', back_populates='home_team', cascade='all')
    away_game = relationship('Game', foreign_keys='Game.away_id', back_populates='away_team', cascade='all')

    def __repr__(self):
        return f'<Team(name={self.team_name})>'


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    home_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    away_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    date = Column(Date)
    time = Column(Time)
    home_score = Column(Integer)
    away_score = Column(Integer)
    home_team = relationship('Team', foreign_keys='Game.home_id', back_populates='home_game')
    away_team = relationship('Team', foreign_keys='Game.away_id', back_populates='away_game')

    def __repr__(self):
        return f'<Game({home_id} vs {away_id} @ {home_score} - {away_score}) on {date}>'


# create the table in our db
engine = create_mysql_engine()
Base.metadata.create_all(engine)

# the schema can be created by entering the flask container and run 'import flaskapp.model.nba' in python environment.