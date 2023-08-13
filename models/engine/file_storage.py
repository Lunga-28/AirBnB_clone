#!/usr/bin/python3
"""
This is for storing data
"""
import json
import models


class FileStorage:
    """
    .....
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        ......
        """
        return (self.__objects)

    def new(self, obj):
        """
        sets key id
        """
        if obj:
            self.__objects["{}.{}".format(str(type(obj).__name__),
                                          obj.id)] = obj

    def save(self):
        """
        ....
        """
        dicc = {}
        for id, objs in self.__objects.items():
            dicc[id] = objs.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as myfile:
            json.dump(dicc, myfile)

    def reload(self):
        """
        ...
        """
      
        try:
            with open(self.__file_path, encoding="UTF-8") as myfile:
                obj = json.load(myfile)
            for key, value in obj.items():
                name = models.allclasses[value["__class__"]](**value)
                self.__objects[key] = name
        except FileNotFoundError:
            pass
