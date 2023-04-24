# Writing a file
file = open("sample.txt", "w")
file.write("Hello, World!")
file.close()

# Open the files
file = open("sample.txt", "r")
contents = file.read()
print(contents)

# Appending the file
file = open("sample.txt", "a")
file.write("This is a new line.")
file.close()

# File handling with `with` context
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)