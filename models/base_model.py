"""
models/base_model.py
Module containing the base model class
"""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        If kwargs is not empty:
        - Each key of this dictionary is an attribute name (excluding __class__).
        - Each value of This dictionary is the value of the respective atrribute.
        - converts created_at and uodated_at from string to datetime objects

        otherwise:
        - creates id and created_at as done previously (new instance).
        """
        if kwargs:
            for key, value in kwargs.items.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of of the BaseModel Instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel Instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
