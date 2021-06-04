# Parent Class
class Person:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def print_name(self):
        print(self.first_name, self.last_name)  # Returns Jane Doe


# Use the Person class to create an object, and then execute the print_name method:
x = Person("Jane", "Doe")
x.print_name()


# Child Class
class Student(Person):
    def __init__(self, fi_name, la_name, year):
        # By using the super() function, you do not have to use the name of the parent element, it will automatically
        # inherit the methods and properties from its parent.
        super().__init__(fi_name, la_name)
        self.graduation_year = year

    def welcome(self):
        print("Welcome", self.first_name, self.last_name, "to the class of", self.graduation_year, ".")
        # Returns Welcome Kurt Weller to the class of 2021 .


# Use the Student class to create an object, and then execute the welcome method:
y = Student("Kurt", "Weller", 2021)
y.welcome()
