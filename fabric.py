from json_serializer import JsonSerializer


class Fabric:
    @staticmethod
    def create_serializer(self, str):
        if str == "Json":
            return JsonSerializer
        else:
            return None
