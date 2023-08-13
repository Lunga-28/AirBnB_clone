#!/usr/bin/python3
import uuid
from datetime import datetime
import models

"""
for all the models
"""


class BaseModel:
    """
    Instantiation of class BaseModel
    """

  
    def __init__(self, *args, **kwargs):
        """
        init
        """
      
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                  
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        handles string returns
        """
        return ("[{}] ({}) {}".format(str(type(self).__name__),
                                      self.id, str(self.__dict__)))

    def __repr__(self):
        """
        for returns
        """
        ccls = self.__class__.__name__
        string = ("[{}] ({}) {}".format(ccls, self.id, self.__dict__))
        return (string)

    def save(self):
        """
        saves and update
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        return key
        """
      
        dicc = dict(**self.__dict__)
        dicc['__class__'] = str(type(self).__name__)
        dicc['created_at'] = self.created_at.isoformat()
        dicc['updated_at'] = self.updated_at.isoformat()

        return (dicc)
