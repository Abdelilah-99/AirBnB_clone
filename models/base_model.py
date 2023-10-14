#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """Define all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """instantiate an instance"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        models.storage.new(self)

        if kwargs is not {} or None:
            for key, value in kwargs.items():
                if key in ("created_at, updated_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    if key == "id":
                        self.__dict__[key] = str(value)
                    else:
                        self.__dict__[key] = value

    def __str__(self):
        """Print the class's name, id and dict"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the instance attribute"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary representation of an instance"""
        class_name = self.__class__.__name__
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = class_name
        return obj_dict