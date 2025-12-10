# Errors in python
# 1- compilation error (syntax erros)
# 2- logical error
# 3- runtime error

# Errors
# 1- ZeroDivisionError
# 2- Exception
# 3- ValueError
# 4- IndexError
# 4- KeyError
# 5- TypeError
# 6- NameError
# 7- AttributeError
# 8- ImportError
# 9- FileNotFoundError
# 10- IndentationError
# 11- ModuleNotFoundError
# 12- StopIteration
# 13- OverflowError
# 14- RecursionError
# 15- MemoryError
# 16- AssertionError
# 17- FloatingPointError
# 18- EOFError and more


try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except ZeroDivisionError as e:
    print("You can't divide a number by zero.", e)
except ValueError as e:
    print("Invalid input. Please enter numeric values only.", e)
except Exception as e:
    print("Something went wrong.", e)
finally:
    print("This will always execute.")


def check_password_strength(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")
    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter.")
    if "-" in password:
        raise Exception("Error: Password cannot contain hyphens.")
    return "Password is strong."


try:
    user_password = input("Enter your password: ")
    print(check_password_strength(user_password))
except ValueError as ve:
    print("Password Error:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)

# File handling in python
# 1- open() function
# 2- read() function
# 3- readline() function
# 4- readlines() function
# 5- write() function
# 6- writelines() function
# 7- close() function
# 8- with statement
