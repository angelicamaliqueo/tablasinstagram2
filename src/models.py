import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    last_name = Column(String(120), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), unique=False, nullable=False)
    fecha_nacimiento = Column(String(120), unique=False, nullable=False)
    imagen_perfil = Column(String(120), unique=False, nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
 

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_type = Column(String(120))
    post_place = Column(String(120))
    post_comment = Column(String(120))
    created_at = Column(String(120))
    updated_at = Column(String(120))

class Posts_comentario(Base):
    __tablename__ = 'posts_comentario'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    comment = Column(String(120))
    created_at = Column(String(120))
    delete_at = Column(String(120))

class Post_likes(Base):
    __tablename__ = 'post_likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    created_at = Column(String(120))
    delete_at = Column(String(120))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')