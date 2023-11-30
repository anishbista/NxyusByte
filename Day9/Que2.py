import json


class Serializer:
    @staticmethod
    def serialize_data(data):
        return json.dumps(data)

    @staticmethod
    def deserialize_data(serialized_data):
        return json.loads(serialized_data)


data = {"name": "Alice", "age": 25, "city": "London"}


serialized = Serializer.serialize_data(data)
print("Serialized data:", serialized)


deserialized = Serializer.deserialize_data(serialized)
print("Deserialized data:", deserialized)
