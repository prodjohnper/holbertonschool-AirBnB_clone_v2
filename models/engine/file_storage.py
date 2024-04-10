#!/usr/bin/python3
'''
    FileStorage class that serializes instances to a
    JSON file and deserializes JSON file to instances
'''
import json


class FileStorage:
    '''
        Serializes instances to a JSON file and deserializes JSON file to instances
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        '''
            Returns the dictionary __objects
        '''
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_objects = {}
            for key, value in FileStorage.__objects.items():
                if isinstance(value, cls):
                    filtered_objects[key] = value
            return filtered_objects

    def new(self, obj):
        '''
            Sets in __objects the obj with key <obj class name>.id
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
            Serializes __objects to the JSON file (path: __file_path)
        '''
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        '''
            Deserializes the JSON file to __objects
        '''
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name = val['__class__']
                    obj = classes[class_name](**val)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        '''
            Delete obj from __objects if it’s inside
        '''
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def close(self):
        '''
            Call reload() method for deserializing the JSON file to objects
        '''
        self.reload()
