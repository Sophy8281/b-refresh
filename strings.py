# Get the character at position 1
a = "Hello, World!"
print(a[1])  # returns e

# Substring. Get the characters from position 0 to position 4
print(a[0:4])  # returns Hell

# Remove any whitespace from the beginning or the end using he strip() method
b = "                    Hello, World!                       "
print(b.strip())  # returns Hello, World!

#  Length of a string
print(len(a))  # returns 13

# Convert a string into lower case
print(a.lower())  # returns hello, world!

# Convert a string into upper case
print(a.upper())  # returns HELLO, WORLD!

# Replace a string with another string
print(a.replace("H", "J"))  # returns Jello, World!

# Split a string into substrings
print(a.split(","))  # returns ['Hello', ' World!']

# Command-line string input
print("Enter your name:")
x = input()
print("Hello, " + x)
