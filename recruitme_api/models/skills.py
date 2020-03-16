#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Skill(BaseModel, Base):
    """This is the class for user
    Attributes:
        lang: Programming lenguages that the user handle
    """

    __tablename__ = 'skills'
    Python = Column(Integer, nullable=True)
    Java = Column(Integer, nullable=True)
    C = Column(Integer, nullable=True)
    C_plus_plus = Column(Integer, nullable=True)
    JavaScript = Column(Integer, nullable=True)
    Go = Column(Integer, nullable=True)
    R = Column(Integer, nullable=True)
    Swift = Column(Integer, nullable=True)
    PHP = Column(Integer, nullable=True)
    C_sharp = Column(Integer, nullable=True)
    MATLAB = Column(Integer, nullable=True) 
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
