# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, Text, text, Date
from sqlalchemy.ext.declarative import declarative_base

from renbroc import db


Base = declarative_base()
metadata = Base.metadata


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(120), index=True, unique=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.username)


class ClickstreamAgg(db.Model):
    __tablename__ = 'clickstream_agg'

    id = Column(Integer, primary_key=True)
    url_id = Column(Integer, nullable=False, index=True)
    date_click = Column(Date, nullable=False, index=True)
    click_count = Column(Integer, nullable=False)


class Comment(db.Model):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    url_id = Column(Integer, nullable=False, index=True)
    url_text = Column(String(255), nullable=False, index=True)
    comment = Column(Text, nullable=False)
    actor_id = Column(String(32), nullable=False, index=True)


class CommentAgg(db.Model):
    __tablename__ = 'comment_agg'

    id = Column(Integer, primary_key=True)
    url_id = Column(Integer, nullable=False, index=True)
    actor_id = Column(String(32), nullable=False, index=True)
    comment_count = Column(Integer, nullable=False)



class Newswhip(db.Model):
    __tablename__ = 'newswhip'

    id = Column(Integer, primary_key=True)
    url_id = Column(Integer, nullable=False, index=True)
    link_text = Column(String(255), nullable=False)
    headline = Column(String(128), nullable=False)
    excerpt = Column(Text, nullable=False)
    fb_comment_count = Column(Integer, nullable=False, index=True)
    fb_like_count = Column(Integer, nullable=False, index=True)
    fb_share_count = Column(Integer, nullable=False, index=True)
    fb_total_count_delta = Column(Integer, nullable=False)
    tw_count = Column(Integer, nullable=False, index=True)
    tw_total_count_delta = Column(Integer, nullable=False)
    li_count = Column(Integer, nullable=False, index=True)
    tw_creator = Column(String(20), nullable=False)
    recent_fb_counts = Column(Integer, nullable=False)
    recent_tw_counts = Column(Integer, nullable=False)
    uuid = Column(String(32), nullable=False)
    fake_timestamp = Column(DateTime, nullable=False)
    publication_timestamp_text = Column(String(32), nullable=False)
    publication_datetime = Column(DateTime, nullable=False)
    image_link = Column(String(255), nullable=False)
    has_video = Column(Integer, nullable=False)


class NewswhipTopic(db.Model):
    __tablename__ = 'newswhip_topic'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    num_articles = Column(Integer, nullable=False)


class NewswhipTopicSet(db.Model):
    __tablename__ = 'newswhip_topic_set'

    id = Column(Integer, primary_key=True)
    newswhip_id = Column(Integer, nullable=False)
    topic_id = Column(Integer, nullable=False)


class Url(db.Model):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    url_raw = Column(String(255), nullable=False, index=True)
    comment_count = Column(Integer, nullable=False)
    visit_count = Column(Integer, nullable=False)
