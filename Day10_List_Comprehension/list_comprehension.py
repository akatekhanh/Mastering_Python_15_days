# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)

# List comprehension with condition
numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# Another list comprehension with condition
numbers = [1, 2, 3, 4, 5]
even_or_odd = ['even' if x % 2 == 0 else 'odd' for x in numbers]
print(even_or_odd)

# Nested List comprehension
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
pairs = [(x, y) for x in numbers for y in letters]
print(pairs)

# Another
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
filtered_pairs = [(x, y) for x in numbers for y in letters if x != 2 and y != 'b']
print(filtered_pairs)


