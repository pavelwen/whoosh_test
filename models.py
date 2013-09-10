#encoding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, Unicode, DateTime, Boolean, Float, Text, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship, backref

from settings import DATABASE_URI

db = create_engine(DATABASE_URI, echo=False, client_encoding="utf-8")
Session = scoped_session(sessionmaker(bind=db))




Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title  = Column(Unicode(100))
    content = Column(UnicodeText)
    email = Column(Unicode(255))
    contacter = Column(Unicode(100))
    qq = Column(Unicode(20))
    mobile_phone = Column(Unicode(25))
    phone = Column(Unicode(25))
    start_date = Column(Unicode(20))
    end_date = Column(Unicode(20))
    created_at = Column(Unicode(20))
    hits = Column(Integer)
    url = Column(Unicode(255))
    address = Column(Unicode(255))
    post_id = Column(Integer)


if __name__ == '__main__':


	Base.metadata.drop_all(db)
	Base.metadata.create_all(db)

