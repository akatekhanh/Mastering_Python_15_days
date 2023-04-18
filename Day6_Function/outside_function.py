x = 0

def increment_x():
    global x
    x += 1

print(x)        # Output: 0
increment_x()
print(x)        # Output: 1
increment_x()
print(x)        # Output: 2