"""

"""
import json

class FileStorage:
    __fle_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with the key <obj class name>.id.
        """
        key = "{}.{}". format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

        def save(self):
            """
            Serializes __objects to the JSON file (path: __file_path).
            """
            serialized_objects = {}
            for key, obj in self.__objects.items():
                serialized_objects[key] = obj.to_dict()

            with open(self.__file_path, 'w') as file:
                json.dump(serialized_objects, file)
        def reload(self):
            """
            Deserializes the JSON file to __objects (only if the file exists)
            """
            try:
                with open(self._file_path, 'i') as file:
                    data = json.load(file)
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        obj = eval((class_name)(**value)
                        self.__objects[key] = obj
            except FileNotFoundError:
                pass
