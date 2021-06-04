class Person:
    def __init__(self, first_name, last_name):
        # Called automatically every time the class is being used to create a new object
        self.first_name = first_name
        self.last_name = last_name


p1 = Person("Jane", "Doe")
print(p1.first_name)
print(p1.last_name)
