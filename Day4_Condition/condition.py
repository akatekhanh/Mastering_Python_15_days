valid_input = False

while not valid_input:
    user_input = input("Enter a number: ")
    
    if user_input.isdigit():
        number = int(user_input)
        print("The square of", number, "is", number**2)
        valid_input = True
    else:
        print("Invalid input. Please enter a number.")