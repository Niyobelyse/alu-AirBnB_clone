#!/usr/bin/python3
"""
This File defines the BaseModel class that will
serve as the base class for all our models.
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base class for all our classes"""

    def __init__(self, *args, **kwargs):
        """Constructor: it either deserializes
        a serialized class or initializes a new one."""

        # Initialize a new instance if no kwargs are passed
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            # Deserialize an instance from kwargs
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, val)
            
            # Handle date fields
            self.created_at = datetime.strptime(
                kwargs.get('created_at'), '%Y-%m-%dT%H:%M:%S.%f'
            ) if 'created_at' in kwargs else datetime.utcnow()

            self.updated_at = datetime.strptime(
                kwargs.get('updated_at'), '%Y-%m-%dT%H:%M:%S.%f'
            ) if 'updated_at' in kwargs else datetime.utcnow()

    def __str__(self):
        """Override the string representation of the instance"""
        return "[{}] ({}) {}".format(
            type(self).__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Updates the updated_at attribute and saves the instance"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        temp = self.__dict__.copy()
        temp['__class__'] = type(self).__name__
        temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        temp['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return temp

    @classmethod
    def all(cls):
        """Retrieve all current instances of the class"""
        return models.storage.find_all(cls.__name__)

    @classmethod
    def count(cls):
        """Get the number of all current instances of the class"""
        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def create(cls, *args, **kwargs):
        """Create an instance and return its id"""
        new_instance = cls(*args, **kwargs)
        models.storage.new(new_instance)
        models.storage.save()
        return new_instance.id

    @classmethod
    def show(cls, instance_id):
        """Retrieve a specific instance by its ID"""
        return models.storage.find_by_id(cls.__name__, instance_id)

    @classmethod
    def destroy(cls, instance_id):
        """Delete an instance by its ID"""
        return models.storage.delete_by_id(cls.__name__, instance_id)

    @classmethod
    def update(cls, instance_id, *args):
        """Update an instance's attributes
        If args contains a single dictionary, update using key-value pairs.
        Otherwise, treat args as key-value pairs."""
        
        instance = cls.show(instance_id)
        if not instance:
            print("** no instance found **")
            return
        
        if len(args) == 1 and isinstance(args[0], dict):
            updates = args[0].items()
        elif len(args) >= 2:
            updates = [args[:2]]
        else:
            print("** attribute name missing **")
            return

        for key, value in updates:
            setattr(instance, key, value)

        instance.save()
