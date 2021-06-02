# Creating a list
simple_list = ["apple", "banana", "cherry"]
print("Simple List")
print(simple_list)  # Returns ['apple', 'banana', 'cherry']
print("-----------------------------------")
print("After changing item 3")
simple_list[2] = "blackcurrant"
print(simple_list)  # Returns ['apple', 'banana', 'blackcurrant']
print("-----------------------------------")

# The list() Constructor
print("Using the list() constructor")
# note the double round-brackets
this_list = list(("apple", "banana", "cherry"))
print(this_list)  # Returns ['apple', 'banana', 'cherry']
print("Length of the list")
print(len(this_list))  # Returns 3
print("-----------------------------------")

# Appending an item
this_list.append("pineapple")
print("After appending an item")
print(this_list)  # Returns ['apple', 'banana', 'cherry', 'pineapple']
print("-----------------------------------")

# Removing an item
this_list.remove("apple")
print("After removing an item")
print(this_list)  # Returns ['banana', 'cherry', 'pineapple']
print("-----------------------------------")
