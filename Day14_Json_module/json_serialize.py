import json

person = {"name": "John Doe", "age": 30, "city": "New York"}

# Serialize the dictionary to a JSON-formatted string
json_string = json.dumps(person)

print(json_string)
# {"name": "John Doe", "age": 30, "city": "New York"}


## Another example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def toJSON(self):
        return {"name": self.name, "age": self.age}

person = Person("John Doe", 30)

# Use the toJSON() method to serialize the object to JSON
json_string = json.dumps(person, default=lambda x: x.toJSON())

print(json_string)