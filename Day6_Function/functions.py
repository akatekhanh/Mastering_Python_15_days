# Add 2 numbers
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum


# Print
def greet(name, greeting='Hello'):
    print(f'{greeting}, {name}!')

# Calculate rectangle
def rectangle_area(width, height):
    area = width * height
    return area


total = add_numbers(1, 3)
print(total)

greet("GeeksData.pro")

area = rectangle_area(3, 4)
print(area)