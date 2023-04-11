# A tuple is a collection of ordered and immutable elements. 

# Access Tuple
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])    # Output: "apple"
print(my_tuple[-1])   # Output: "cherry"

# Slicing
my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
print(my_tuple[1:4])     # Output: ("banana", "cherry", "orange")
print(my_tuple[:4])      # Output: ("apple", "banana", "cherry", "orange")
print(my_tuple[4:])      # Output: ("kiwi", "melon")
print(my_tuple[-3:-1])   # Output: ("orange", "kiwi")

# Concat
my_tuple1 = ("apple", "banana", "cherry")
my_tuple2 = ("orange", "kiwi", "melon")
my_tuple3 = my_tuple1 + my_tuple2
print(my_tuple3)   # Output: ("apple", "banana", "cherry", "orange", "kiwi", "melon")

# Multiplying
my_tuple = ("apple", "banana", "cherry")
my_tuple2 = my_tuple * 3
print(my_tuple2)   # Output: ("apple", "banana", "cherry", "apple", "banana", "cherry", "apple", "banana", "cherry")