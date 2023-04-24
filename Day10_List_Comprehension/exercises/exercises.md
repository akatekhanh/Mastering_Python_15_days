## Exercises

1. Write a list comprehension that squares each number in a list of integers.

```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)
```

1. Write a list comprehension that filters out all the even numbers from a list of integers.

```python
numbers = [1, 2, 3, 4, 5]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)
```

1. Write a list comprehension that flattens a list of lists.

```python
nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [x for sublist in nested_lists for x in sublist]
print(flat_list)
```

1. Write a list comprehension that extracts the first character of each word in a list of strings.

```python
words = ['apple', 'banana', 'cherry']
first_letters = [word[0] for word in words]
print(first_letters)
```

1. Write a list comprehension that filters out all the vowels from a string.

```python
string = 'Hello, World!'
consonants = [char for char in string if char.lower() not in 'aeiou']
print(''.join(consonants))

```
