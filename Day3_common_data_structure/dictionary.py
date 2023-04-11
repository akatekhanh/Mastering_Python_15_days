# A dictionary is a collection of key-value pairs, where each key is unique and corresponds to a value. 

my_dict = {"name": "John", "age": 30}
my_dict["city"] = "New York"
my_dict["age"] = 31
print(my_dict)   # Output: {"name": "John", "age": 31, "city": "New York"}

# Remove element
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Using del
del my_dict["age"]
print(my_dict)   # Output: {"name": "John", "city": "New York"}

# Using pop
my_dict.pop("city")
print(my_dict)   # Output: {"name": "John"}

# Accessing element
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Accessing keys
print(my_dict.keys())   # Output: dict_keys(["name", "age", "city"])

# Accessing values
print(my_dict.values())   # Output: dict_values(["John", 30, "New York"])