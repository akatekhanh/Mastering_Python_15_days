try:
    # code that may raise an exception
    value = 1/0
except ValueError:
    # code to handle a ValueError
    print(ValueError)
except ZeroDivisionError:
    # code to handle a ZeroDivisionError
    pass
except:
    # code to handle any other exception
    print("unknown errors")
finally:
    print("Finally statement")
