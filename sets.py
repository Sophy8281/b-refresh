# Creating a Set
this_set = {"apple", "banana", "cherry"}
print("A simple set")
print(this_set)  # Returns {'apple', 'banana', 'cherry'}
print("-------------------------------------------------")

# Using the set() constructor to make a set
this_set = set(("apple", "banana", "cherry"))  # note the double round-brackets
print("Using the set() constructor to make a set")
print(this_set)  # Returns {'apple', 'banana', 'cherry'}
print("-------------------------------------------------")

# Adding an item
this_set.add("damson")
print("After adding an item")
print(this_set)  # Returns {'cherry', 'damson', 'apple', 'banana'}
print("-------------------------------------------------")

# Removing an item
this_set.remove("banana")
print("After removing an item")
print(this_set)  # Returns {'cherry', 'damson', 'apple'}
print("-------------------------------------------------")

# Length of the set
print("Length of the set")
print(len(this_set))  # Returns 3
print("-------------------------------------------------")
