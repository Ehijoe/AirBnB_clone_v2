#!/usr/bin/python3
"""Database storage module."""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

HBNB_MYSQL_USER = os.getenv("HBNB_MYSQL_USER")
HBNB_MYSQL_PWD = os.getenv("HBNB_MYSQL_USER")
HBNB_MYSQL_HOST = os.getenv("HBNB_MYSQL_USER")
HBNB_MYSQL_DB = os.getenv("HBNB_MYSQL_USER")
HBNB_ENV = os.getenv("HBNB_ENV")


class DBStorage:
    """Class for Database storage."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database storage."""
        from models.base_model import Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        self.__engine = create_engine(
            "mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db",
            pool_pre_ping=True,
        )
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        Base.metadata.create_all(self.__engine)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)
