#!/usr/bin/python3
"""DBstorage module
"""

import os
from models.base_model import BaseModel, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.user import User
from models.skills import Skill

class DBStorage:
    '''DBStorage class'''

    __engine = None
    __session = None

    RECRUITME_MYSQL_USER = 'RecruitMe_dev'
    RECRUITME_MYSQL_PWD = 'RecruitMe_dev_pwd'
    RECRUITME_MYSQL_HOST = 'localhost'
    RECRUITME_MYSQL_DB = 'RecruitMe_dev_db'

    def __init__(self):
        '''To initialize an DBStorage instance'''

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(DBStorage.RECRUITME_MYSQL_USER,
                   DBStorage.RECRUITME_MYSQL_PWD,
                   DBStorage.RECRUITME_MYSQL_HOST,
                   DBStorage.RECRUITME_MYSQL_DB),
            pool_pre_ping=True)

        #if os.getenv("RECRUITME_ENV") == 'test':
            #Base.metadata.drop_all(bind=self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def all(self, cls=None):
        '''Query on the current Db session all objects depending on
        the class name
        Return:
        Dictionary where
        key = <class-name>.<object-id>
        value = obj
        '''

        Dict = {}

        if cls:

            for instance in self.__session.query(cls):
                key = '{}.{}'.format(type(instance).__name__, instance.id)
                Dict[key] = instance

            return Dict

        else:

            for instance in self.__session.query(User):
                key = '{}.{}'.format(type(instance).__name__, instance.id)
                Dict[key] = instance

            for instance in self.__session.query(Skill):
                key = '{}.{}'.format(type(instance).__name__, instance.id)
                Dict[key] = instance

        return Dict

    def new(self, obj):
        '''Add new obj to the current database session'''

        if obj:
            self.__session.add(obj)

    def save(self):
        '''commit all changes to the current database session'''

        self.__session.commit()

    def delete(self, obj=None):
        '''Delete current db session obj if not None'''

        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        '''Reload all the database'''

        Base.metadata.create_all(self.__engine)
