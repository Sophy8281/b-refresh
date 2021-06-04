# Using slice
txt = "Hello World"[::-1]
print("The reversed string(using slice) is : ", end="")
print(txt)  # Returns dlroW olleH


# Using reverse keyword
def reverse(s):
    string = ""
    for i in s:
        string = i + string
    return string


s = "Sophia"
print("The original string  is : ", end="")
print(s)  # Returns Sophia
print("The reversed string(using reverse keyword) is : ", end="")
print(reverse(s))  # Returns aihpoS
