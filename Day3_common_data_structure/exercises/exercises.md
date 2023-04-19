# Day 3: Common data Structure in Python: List, Set, Tuple and Dictionary

## 1. Introduction

## 2. List, Tuple, Set and Dictionary

### 2.1 List

> A list is a collection of items that are `ordered` and `changeable`.
> 

Lists are created using square brackets [] and each item in the list is separated by a comma. 

You can access and manipulate elements of a list using its index. Some common operations you can perform on lists include appending, slicing, sorting, and removing elements.

Here's an example of how to create a list in Python:

```python
fruits = ["apple", "banana", "cherry"]
```

List has some common actions you can get perform on a list in Python

1. Accessing Elements

You can access individual elements of a list using its index. The index of the first element is 0, and the index of the last element is -1. Here's an example:

```python
my_list = ["apple", "banana", "cherry"]
print(my_list[0])    # Output: "apple"
print(my_list[-1])   # Output: "cherry"
```

1. Modify Elements

You can modify individual elements of a list using their index. Here's an example:

```python
my_list = ["apple", "banana", "cherry"]
my_list[1] = "orange"
print(my_list)   # Output: ["apple", "orange", "cherry"]
```

1. Slicing

You can extract a subset of a list using slicing. Slicing uses the colon operator to specify a range of indices. Here's an example:

```python
my_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon"]
print(my_list[1:4])     # Output: ["banana", "cherry", "orange"]
print(my_list[:4])      # Output: ["apple", "banana", "cherry", "orange"]
print(my_list[4:])      # Output: ["kiwi", "melon"]
print(my_list[-3:-1])   # Output: ["orange", "kiwi"]
```

1. Appending Elements

You can add elements to the end of a list using the append() method. Here's an example:

```python
my_list = ["apple", "banana", "cherry"]
my_list.append("orange")
print(my_list)   # Output: ["apple", "banana", "cherry", "orange"]
```

1. Extending a List

```python
my_list = ["apple", "banana", "cherry"]
my_list.extend(["orange", "kiwi", "melon"])
print(my_list)   # Output: ["apple", "banana", "cherry", "orange", "kiwi", "melon"]
```

1. Inserting an Element

```python
my_list = ["apple", "banana", "cherry"]
my_list.insert(1, "orange")
print(my_list)   # Output: ["apple", "orange", "banana", "cherry"]
```

1. Removing an Element

You can remove an element from a list using the remove() method. If the element appears multiple times in the list, only the first occurrence will be removed. Here's an example:

```python
my_list = ["apple", "banana", "cherry"]
my_list.remove("banana")
print(my_list)   # Output: ["apple", "cherry"]
```

1. Pop an Element

You can remove and return the last element of a list using the pop() method. You can also specify an index to remove and return a specific element. Here's an example:

```python
my_list = ["apple", "banana", "cherry"]
my_list.pop()     # Output: "cherry"
my_list.pop(1)    # Output: "banana"
print(my_list)    # Output: ["apple"]
```

### 2.2 Tuple

> A tuple is a collection of `ordered` and `immutable` elements.
> 

Tuples are created using parentheses () and each element is separated by a comma. You can access and manipulate elements of a tuple using its index, but you cannot modify its values.

Here’s an example of how to create a tuple in Python

```python
person = ("John", 25, "Male")
```

`***NOTE***` you cannot modify the elements of a tuple once it is created, as tuples are immutable. This means that you cannot append, remove or modify elements in a tuple.

1. Accessing Elements

You can access individual elements of a tuple using its index. The index of the first element is `0`, and the index of the last element is `-1`. Here's an example:

```python
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])    # Output: "apple"
print(my_tuple[-1])   # Output: "cherry"
```

1. Slicing

You can extract a subset of a tuple using slicing. Slicing uses the colon operator to specify a range of indices. Here's an example:

```python
my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
print(my_tuple[1:4])     # Output: ("banana", "cherry", "orange")
print(my_tuple[:4])      # Output: ("apple", "banana", "cherry", "orange")
print(my_tuple[4:])      # Output: ("kiwi", "melon")
print(my_tuple[-3:-1])   # Output: ("orange", "kiwi")
```

3. Concatenating Tuples:

You can concatenate two or more tuples using the + operator. Here's an example:

```python
my_tuple1 = ("apple", "banana", "cherry")
my_tuple2 = ("orange", "kiwi", "melon")
my_tuple3 = my_tuple1 + my_tuple2
print(my_tuple3)   # Output: ("apple", "banana", "cherry", "orange", "kiwi", "melon")
```

1. Multiplying a Tuple:

```python
my_tuple = ("apple", "banana", "cherry")
my_tuple2 = my_tuple * 3
print(my_tuple2)   # Output: ("apple", "banana", "cherry", "apple", "banana", "cherry", "apple", "banana", "cherry")
```

### 2.3 Set

> A set is an `unordered` collection of unique elements.
> 

Sets are created using curly braces {} or the set() function. You can perform various operations on sets, such as union, intersection, difference, and symmetric difference.

Here's an example of how to create a set in Python:

```python
colors = {"red", "green", "blue"}
```

Some actions in `Set` in Python the same with `Tuple` or `List`

Sets support various set operations like union, intersection, difference and symmetric difference. Here are some examples:

```python
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

```

### 2.4 Dictionary

> A dictionary is a collection of key-value pairs, where each key is unique and corresponds to a value.
> 

Dictionaries are created using curly braces `{}` and each key-value pair is separated by a colon `:` . You can access and manipulate values of a dictionary using its keys.

Here's an example of how to create a dictionary in Python:

```python
person = {"name": "John", "age": 25, "gender": "Male"}
```

Some actions in `Dictionay`

1. Adding or Modifying Key-Value Pairs:

You can add a new key-value pair to a dictionary or modify an existing one by simply assigning a value to a key. Here's an example:

```python
my_dict = {"name": "John", "age": 30}
my_dict["city"] = "New York"
	my_dict["age"] = 31
print(my_dict)   # Output: {"name": "John", "age": 31, "city": "New York"}
```

1. Removing Key-Value Pairs:

You can remove a key-value pair from a dictionary using the **`del`** keyword or the **`pop()`** method. Here are some examples:

```python
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Using del
del my_dict["age"]
print(my_dict)   # Output: {"name": "John", "city": "New York"}

# Using pop
my_dict.pop("city")
print(my_dict)   # Output: {"name": "John"}
```

**`Note`** that if you try to remove a key that does not exist in the dictionary, a **`KeyError`** will be raised. To avoid this, you can use the **`pop()`** method with a default value that will be returned if the key does not exist in the dictionary.

1. Accessing Keys and Values:

You can access the keys and values of a dictionary using the **`keys()`** and **`values()`** methods, respectively. Here are some examples:

```python
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Accessing keys
print(my_dict.keys())   # Output: dict_keys(["name", "age", "city"])

# Accessing values
print(my_dict.values())   # Output: dict_values(["John", 30, "New York"])
```

1. Checking if a Key Exists:

You can check if a key exists in a dictionary using the **`in`** keyword. Here's an example:

```python
my_dict = {"name": "John", "age": 30, "city": "New York"}
print("name" in my_dict)   # Output: True
print("country" in my_dict)   # Output: False
```

## 3. Exercises

### `List exercises`

1. Create a list **`my_list`** with the following elements:

```
Copy code
1, 2, 3, 4, 5
```

1. Add the element **`6`** to the end of **`my_list`**.
2. Insert the element **`0`** at the beginning of **`my_list`**.
3. Remove the element **`3`** from **`my_list`**.
4. Print the length of **`my_list`**.
5. Print the first three elements of **`my_list`**.
6. Check if the element **`4`** is in **`my_list`**.
7. Create a function **`reverse_list(my_list)`** that takes a list as input and returns a new list with the elements in reverse order. For example, **`reverse_list([1, 2, 3, 4, 5])`** should return **`[5, 4, 3, 2, 1]`**.
8. Create a function **`even_list(my_list)`** that takes a list as input and returns a new list with only the even elements. For example, **`even_list([1, 2, 3, 4, 5])`** should return **`[2, 4]`**.
9. Create a function **`unique_list(my_list)`** that takes a list as input and returns a new list with only the unique elements. For example, **`unique_list([1, 2, 3, 2, 4, 1])`** should return **`[1, 2, 3, 4]`**.

### `Set exercises`

1. Create a set **`my_set`** with the following elements:

```
Copy code
1, 2, 3, 4, 5
```

1. Add the element **`6`** to **`my_set`**.
2. Remove the element **`3`** from **`my_set`**.
3. Create another set **`your_set`** with the following elements:

```
4, 5, 6, 7, 8
```

1. Find the intersection of **`my_set`** and **`your_set`**.
2. Find the union of **`my_set`** and **`your_set`**.
3. Create a function **`unique_set(my_list)`** that takes a list as input and returns a set with only the unique elements. For example, **`unique_set([1, 2, 3, 2, 4, 1])`** should return **`{1, 2, 3, 4}`**.
4. Create a function **`common_set(set1, set2)`** that takes two sets as input and returns a new set that contains the elements that are common to both sets. For example, **`common_set({1, 2, 3}, {2, 3, 4})`** should return **`{2, 3}`**.
5. Create a function **`diff_set(set1, set2)`** that takes two sets as input and returns a new set that contains the elements that are in **`set1`** but not in **`set2`**. For example, **`diff_set({1, 2, 3}, {2, 3, 4})`** should return **`{1}`**.
6. Create a function **`subset_set(set1, set2)`** that takes two sets as input and returns **`True`** if **`set1`** is a subset of **`set2`**, and **`False`** otherwise. For example, **`subset_set({1, 2}, {1, 2, 3})`** should return **`True`**.

### `Tuple exercises`

1. Create a tuple **`my_tuple`** with the following elements:

```
1, 2, 3, 4, 5
```

1. Print the length of **`my_tuple`**.
2. Print the first three elements of **`my_tuple`**.
3. Check if the element **`4`** is in **`my_tuple`**.
4. Create a function **`reverse_tuple(my_tuple)`** that takes a tuple as input and returns a new tuple with the elements in reverse order. For example, **`reverse_tuple((1, 2, 3, 4, 5))`** should return **`(5, 4, 3, 2, 1)`**.
5. Create a function **`even_tuple(my_tuple)`** that takes a tuple as input and returns a new tuple with only the even elements. For example, **`even_tuple((1, 2, 3, 4, 5))`** should return **`(2, 4)`**.
6. Create a function **`unique_tuple(my_tuple)`** that takes a tuple as input and returns a new tuple with only the unique elements. For example, **`unique_tuple((1, 2, 3, 2, 4, 1))`** should return **`(1, 2, 3, 4)`**.
7. Create a function **`concat_tuple(tuple1, tuple2)`** that takes two tuples as input and returns a new tuple that contains all the elements of **`tuple1`** followed by all the elements of **`tuple2`**. For example, **`concat_tuple((1, 2), (3, 4))`** should return **`(1, 2, 3, 4)`**.
8. Create a function **`max_min_tuple(my_tuple)`** that takes a tuple as input and returns a tuple with the maximum and minimum elements. For example, **`max_min_tuple((1, 2, 3, 4, 5))`** should return **`(5, 1)`**.
9. Create a function **`sort_tuple(my_tuple)`** that takes a tuple as input and returns a new tuple with the elements sorted in ascending order. For example, **`sort_tuple((3, 1, 4, 1, 5, 9, 2, 6, 5))`** should return **`(1, 1, 2, 3, 4, 5, 5, 6, 9)`**.

### `Dictionary exercises`

1. Create a dictionary **`my_dict`** with the following key-value pairs:

```python
jsonCopy code
"apple": 2
"banana": 3
"orange": 5
```

1. Add a key-value pair **`"pear": 4`** to **`my_dict`**.
2. Modify the value of **`"banana"`** in **`my_dict`** to **`4`**.
3. Remove the key-value pair **`"apple": 2`** from **`my_dict`**.