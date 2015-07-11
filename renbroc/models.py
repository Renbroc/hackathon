# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, Text, text
from sqlalchemy.ext.declarative import declarative_base

from renbroc import db


Base = declarative_base()
metadata = Base.metadata



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)



class Clickstream(db.Model):
    __tablename__ = 'clickstream'

    id = Column(Integer, primary_key=True)
    stream_order = Column(Integer, nullable=False)
    url_id = Column(Integer, nullable=False)
    wapo_id = Column(Integer, nullable=False)


class Comment(db.Model):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    url_id = Column(Integer, nullable=False)
    url_text = Column(String(255), nullable=False, index=True)
    comment = Column(Text, nullable=False)
    actor_id = Column(String(32), nullable=False)


class Content(db.Model):
    __tablename__ = 'content'

    id = Column(Integer, primary_key=True)
    url_id = Column(Integer, nullable=False)
    url_text = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)


class Newswhip(db.Model):
    __tablename__ = 'newswhip'

    id = Column(Integer, primary_key=True)
    url_id = Column(Integer, nullable=False, index=True)
    link_text = Column(String(255), nullable=False)
    headline = Column(String(128), nullable=False)
    excerpt = Column(Text, nullable=False)
    source_pub = Column(String(32), nullable=False)
    nw_score = Column(Integer, nullable=False)
    max_nw_score = Column(Integer, nullable=False)
    fb_comment_count = Column(Integer, nullable=False, index=True)
    fb_like_count = Column(Integer, nullable=False, index=True)
    fb_share_count = Column(Integer, nullable=False, index=True)
    fb_total_count_delta = Column(Integer, nullable=False)
    fb_delta_period = Column(Integer, nullable=False)
    fb_delta_period_unit = Column(String(4), nullable=False)
    tw_count = Column(Integer, nullable=False, index=True)
    tw_total_count_delta = Column(Integer, nullable=False)
    tw_delta_period = Column(Integer, nullable=False)
    tw_delta_period_unit = Column(String(4), nullable=False)
    li_count = Column(Integer, nullable=False, index=True)
    li_total_count_delta = Column(Integer, nullable=False)
    li_delta_period = Column(Integer, nullable=False)
    li_delta_period_unit = Column(String(4), nullable=False)
    tw_creator = Column(String(20), nullable=False)
    delta_time = Column(Integer, nullable=False)
    recent_fb_counts = Column(Integer, nullable=False)
    recent_tw_counts = Column(Integer, nullable=False)
    uuid = Column(String(32), nullable=False)
    fake_timestamp = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    publication_timestamp_text = Column(String(32), nullable=False)
    publication_timestamp = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    image_link = Column(String(255), nullable=False)
    related_stories = Column(Text, nullable=False)
    has_video = Column(Integer, nullable=False)


class NewswhipTopic(db.Model):
    __tablename__ = 'newswhip_topic'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)


class NewswhipTopicSet(db.Model):
    __tablename__ = 'newswhip_topic_set'

    id = Column(Integer, primary_key=True)
    newswhip_id = Column(Integer, nullable=False)
    topic_id = Column(Integer, nullable=False)


class Url(db.Model):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    url_raw = Column(String(255), nullable=False, index=True)
    url_no_www = Column(String(255), nullable=False, index=True)
    url_no_http_www = Column(String(255), nullable=False, index=True)
    url_filename = Column(String(255), nullable=False)
