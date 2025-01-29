# Simple consoles

print("Hello, Arch Linux!")
print("Here's another console")

# Variables
myName = "Raheel"
my_name = "Raheel"
myname = "Raheel"

print(myName, my_name, myname)

# Data types
my_name = "Janab"
print(my_name)

# Type checking
print(type(my_name))

# Type conversion
my_age = "20"
my_age = int(my_age)
print(my_age)
my_age = float(my_age)
print(my_age)
my_age = str(my_age)
print(my_age)

# Assignment
one, two, three = 1, 2, 3
print(one, two, three)

one = two = three = "Haha! I'm a string"
print(one, two, three)


# Global and local variables
global_var = "global"


def my_func():
    # print(global_var)will create an unbound -- accessing before initilaizing
    global_var = "internal variable"
    print(global_var)


print(global_var)
my_func()

# NOTE: global variables can be used inside functions, but if you reasign it, global will not be affected (when you create a variable inside a function, that variable is local, and can only be used inside that function)

# The global keyword


def another_function():
    global a_random_number  # makes a_random_number global
    a_random_number = 20
    print(a_random_number)


# print(a_random_number)will give error if you try to access it before calling the function
another_function()
print(a_random_number)


# Brief on data types
# Strings
a_string = "Hello, Arch Linux!"

print(a_string)
print(type(a_string))

# Multiple lines
a_string = """Hello, Arch Linux!
Here's another console
Raheel Raheel Raheel
Janab
"""

print(a_string)
print(type(a_string))
