# Creating a dictionary
dictionary = {"apple": "red", "banana": "yellow", "cherry": "red"}
print("Simple Dictionary")
print(dictionary)
print("Length of dictionary")
print(len(dictionary))  # Length of dictionary
print("-------------------------------------------------------------")

# The dict() Constructor
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
this_dict = dict(apple="green", banana="yellow", cherry="red")
print("Dictionary using the dict() Constructor")
print(this_dict)
print("Length of dictionary")
print(len(this_dict))  # Length of this_dict

this_dict["damson"] = "purple"  # Adding an item
print("-------------------------------------------------------------")
print("After adding an item ")
print(this_dict)

del (this_dict["banana"])  # Removing an item
print("-------------------------------------------------------------")
print("After removing an item ")
print(this_dict)
print("-------------------------------------------------------------")
