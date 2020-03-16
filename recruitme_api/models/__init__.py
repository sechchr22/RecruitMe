#!/usr/bin/python3
"""create a unique Dbstorage instance for RecruitMe app"""
from models.base_model import BaseModel
from models.user import User
from models.skills import Skill
from engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
