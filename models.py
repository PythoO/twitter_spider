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

    def __repr__(self):
        return "<Accounts(name= '%s', user_id='%d')>" % (self.name, self.user_id)


class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    tid = Column(Integer)
    # Foreign key
    uid = Column(Integer)
    favorite_count = Column(Integer)
    retweet_count = Column(Integer)
    text = Column(String)

engine = sqla.create_engine('sqlite:///tutorial.db', echo=False)
connection = engine.connect()
Session = sessionmaker()
Base.metadata.create_all(engine)
Session.configure(bind=engine)
session = Session()
