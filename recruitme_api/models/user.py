#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        name: user name
        email: email address
        password: password for user login
        whatsapp: user whatsapp
        github: user githubaccount
    """

    __tablename__ = 'users'
    name = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    github = Column(String(128), nullable=False)
    whatsapp = Column(String(128), nullable=False)
    skills = relationship('Skill', backref='user', cascade='all, delete')
