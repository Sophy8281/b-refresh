# Creating a Tuple
this_tuple = ("apple", "banana", "cherry")
print("A simple tuple")
print(this_tuple)  # Returns ('apple', 'banana', 'cherry')
print("------------------------------------")

# Getting the item in position 1
this_tuple = ("apple", "banana", "cherry")
print("Getting the item in position 1")
print(this_tuple[1])  # Returns banana
print("------------------------------------")

# Using the tuple() Constructor
this_tuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print("Using the tuple() Constructor")
print(this_tuple)  # Returns ('apple', 'banana', 'cherry')
print("------------------------------------")

# Length of the tuple
this_tuple = tuple(("apple", "banana", "cherry"))
print("Length of the tuple")
print(len(this_tuple))  # Returns 3
print("------------------------------------")
