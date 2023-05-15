#!/usr/bin/python3
""" File storage class """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{ obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                _dict = json.load(f)
                for obj_dict in _dict.values():
                    cls_name = obj_dict["__class__"]
                    del obj_dict["__class__"]
                    self.new(eval(cls_name)(**obj_dict))
        except FileNotFoundError:
            return
