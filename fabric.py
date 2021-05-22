from json_serializer import JsonSerializer
from pickle_serializer import PickleSerializer


class Fabric:
    @staticmethod
    def create_serializer(string):
        if string == "Json":
            return JsonSerializer
        elif string == "Pickle":
            return PickleSerializer
        else:
            return None
