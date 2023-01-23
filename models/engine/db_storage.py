#!/usr/bin/python3
"""Database storage module."""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session

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

        self.classes = {cls.__name__: cls for cls in
                        [Amenity, City, Place, Review, State, User]}

        self.__engine = create_engine(
            "mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db",
            pool_pre_ping=True,
        )
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a dictionary of the existing objects."""
        if cls in self.classes:
            objs = self.__session.query(self.classes[cls]).all()
        elif cls is None:
            objs = self.__session.query().all(self.classes.values())
        else:
            raise ValueError("Invalid class name")
        return {f"{obj.__class__.__name}.{obj.id}": obj for obj in objs}

    def save(self):
        """Commit changes in session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object if given."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload objects from the database."""
        from models.base_model import Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine),
                                        expire_on_commit=False)
