import math

# Using math.pi to get the value of pi
print(math.pi)  # Output: 3.141592653589793

# Using math.ceil() to round up a number to the nearest integer
print(math.ceil(4.2))  # Output: 5

# Using math.floor() to round down a number to the nearest integer
print(math.floor(4.8))  # Output: 4

# Using math.sin() to calculate the sine of an angle in radians
print(math.sin(math.pi/2))  # Output: 1.0

# Using math.cos() to calculate the cosine of an angle in radians
print(math.cos(math.pi))  # Output: -1.0

# Using math.radians() to convert degrees to radians
print(math.radians(180))  # Output: 3.141592653589793

# Using math.degrees() to convert radians to degrees
print(math.degrees(math.pi/2))  # Output: 90.0


## Math in action
radius = 5
area = math.pi * radius ** 2
print(area)  # Output: 78.53981633974483


a = 1
b = 5
c = 6

x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

print(x1, x2)  # Output: -2.0, -3.0