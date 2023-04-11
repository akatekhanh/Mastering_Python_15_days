# A set is an unordered collection of unique elements. A set is an unordered collection of unique elements. 

# Adding Elements
my_set = {"apple", "banana", "cherry"}
my_set.add("orange")
print(my_set)   # Output: {"apple", "banana", "cherry", "orange"}

# Removing Elements
my_set = {"apple", "banana", "cherry"}
my_set.remove("banana")
print(my_set)   # Output: {"apple", "cherry"}

# Checking if an Element Exists
my_set = {"apple", "banana", "cherry"}
print("banana" in my_set)   # Output: True
print("orange" in my_set)   # Output: False

# Set Operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
print(set1 | set2)   # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection
print(set1 & set2)   # Output: {4, 5}

# Difference
print(set1 - set2)   # Output: {1, 2, 3}

# Symmetric Difference
print(set1 ^ set2)   # Output: {1, 2, 3, 6, 7, 8}
