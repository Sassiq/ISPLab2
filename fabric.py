from json_serializer import JsonSerializer


class Fabric:
    @staticmethod
    def create_serializer(string):
        if string == "Json":
            return JsonSerializer
        else:
            return None
