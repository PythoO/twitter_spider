import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    uid = Column(Integer)
    description = Column(String)
    tags = Column(String)
    created_at = Column(Integer)
    updated_at = Column(Integer)

    def __repr__(self):
        return "<Accounts(name= '%s', user_id='%d')>" % (self.name, self.user_id)


class AccountData(Base):
    __tablename__ = "accounts_data"

    id = Column(Integer, primary_key=True)
    uid = Column(Integer)
    favourites_count = Column(Integer)
    followers_count = Column(Integer)
    friends_count = Column(Integer)
    listed_count = Column(Integer)
    statuses_count = Column(Integer)
    created_at = Column(Integer)
    updated_at = Column(Integer)


class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    tid = Column(Integer)
    # Foreign key
    uid = Column(Integer)
    favorite_count = Column(Integer)
    retweet_count = Column(Integer)
    text = Column(String)
    created_at = Column(Integer)
    updated_at = Column(Integer)

engine = sqla.create_engine('sqlite:///tutorial.db', echo=False)
connection = engine.connect()
Session = sessionmaker()
Base.metadata.create_all(engine)
Session.configure(bind=engine)
session = Session()
