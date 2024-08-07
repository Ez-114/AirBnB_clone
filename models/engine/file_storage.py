#!/usr/bin/env python3
"""
models.engine.file_storage.py Module.

This module implements the FileStorage class that helps in storing
a persistent JSON file containing all data about the pre-defined objects
from their classes.
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class.

    Serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attributes:
        - __file_path (str): Path to the JSON file (ex: file.json)
        - __objects (dict): Stores all created objects by <class name>.id

    Methods:
        - all(): Returns the dictionary __objects
        - new(obj): Sets in __objects the obj with key <obj class name>.id
        - save(): Serializes __objects to the JSON file (path: __file_path)
        - reload(): Deserializes the JSON file to __objects
                (only if the JSON file (__file_path) exists;
                        otherwise, do nothing.)
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        FileStorage.all() Instance method.

        Returns:
            dict: the __objects dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        FileStorage.new() Instance method.

        Sets in __objects the obj with key <obj class name>.id
        """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """
        FileStorage.save() Instance method.

        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """
        FileStorage.reload() Instance method.

        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.)
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') \
                    as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    if obj_data['__class__'] == 'BaseModel':
                        FileStorage.__objects[key] = BaseModel(**obj_data)
