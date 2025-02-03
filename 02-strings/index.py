# Strings
# Strings are a sequence of characters

a_simple_string = "Hello, Arch Linux!"
print(a_simple_string)

# Strings can be concatenated
another_string = "Here's another console"
print(another_string + a_simple_string)

# Strings can be indexed
print(a_simple_string[0])
print(a_simple_string[1])
print(a_simple_string[2])
print(a_simple_string[3])
print(a_simple_string[4])
print(a_simple_string[5])

# Strings can be sliced
sliced_string = a_simple_string[0:5]
start_sliced = a_simple_string[0:]
end_sliced = a_simple_string[:5]
negative_sliced = a_simple_string[-5:-2]
print("SLICING ===========>", start_sliced, sliced_string, end_sliced)
print("NEGATIVE =========>", negative_sliced)

# Strings can be repeated
repeated_string = a_simple_string * 3
print(repeated_string)

# Strings can be split
split_string = a_simple_string.split(",")
print(split_string)

# Strings with quotes
a_string_with_quotes = "Hello, 'Arch Linux'!"
print(a_string_with_quotes)

# Multiline strings
multiline_string = """Hello, Arch Linux!
Here's another console
Raheel Raheel Raheel
Janab
"""

print(multiline_string)


# Modifying strings
new_simple_string = "          A quick brown fox jumps over the lazy dog        "

print(new_simple_string)
print(new_simple_string.strip())
print(new_simple_string.upper())
print(new_simple_string.lower())
print(new_simple_string.replace("quick", "slow"))
