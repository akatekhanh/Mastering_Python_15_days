import json

json_string = '{"name": "John Doe", "age": 30, "city": "New York"}'

# Deserialize the JSON-formatted string to a dictionary
person = json.loads(json_string)

print(person)
# {'name': 'John Doe', 'age': 30, 'city': 'New York'}


## Another example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age})"

def fromJSON(json_obj):
    if "name" in json_obj and "age" in json_obj:
        return Person(json_obj["name"], json_obj["age"])
    else:
        return json_obj

json_string = '{"name": "John Doe", "age": 30}'

# Use the fromJSON() function to deserialize the JSON data
person = json.loads(json_string, object_hook=fromJSON)

print(person)
# John Doe (30)