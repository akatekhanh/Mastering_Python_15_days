my_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon"]
print(my_list[1:4])     # Output: ["banana", "cherry", "orange"]
print(my_list[:4])      # Output: ["apple", "banana", "cherry", "orange"]
print(my_list[4:])      # Output: ["kiwi", "melon"]
print(my_list[-3:-1])   # Output: ["orange", "kiwi"] # Output: ["apple", "orange", "cherry"]

# Append
my_list = ["apple", "banana", "cherry"]
my_list.append("orange")
print(my_list)   # Output: ["apple", "banana", "cherry", "orange"]

# Extend 
my_list = ["apple", "banana", "cherry"]
my_list.extend(["orange", "kiwi", "melon"])
print(my_list)   # Output: ["apple", "banana", "cherry", "orange", "kiwi", "melon"]

# Insert operation
my_list = ["apple", "banana", "cherry"]
my_list.insert(1, "orange")
print(my_list)   # Output: ["apple", "orange", "banana", "cherry"]

# Remove operation
my_list = ["apple", "banana", "cherry"]
my_list.remove("banana")
print(my_list)   # Output: ["apple", "cherry"]