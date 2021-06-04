class Person1:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def my_func(self):  # Reference to the current instance of the class (access variables that belong to the class)
        print("Hello my name is " + self.first_name + " " + self.last_name)  # Returns Hello my name is Jane Doe


p1 = Person1("Jane", "Doe")
p1.my_func()


# Using different names (my_object, abc) instead of self
class Person2:
    def __init__(my_object, first_name, last_name):
        my_object.first_name = first_name
        my_object.last_name = last_name

    def my_func(abc):  # Reference to the current instance of the class (access variables that belong to the class)
        print("Hello my name is " + abc.first_name + " " + abc.last_name)  # Returns Hello my name is John Doe


p1 = Person2("Jane", "Doe")
p1.first_name = "John"  # Modifying object properties
p1.my_func()
