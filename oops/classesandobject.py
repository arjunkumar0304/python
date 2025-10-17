class Student:
    # Class attribute
    college_name = "ABC College"

    # Constructor (special method to initialize)
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age

    # Method (function inside class)
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, College: {Student.college_name}")

# Create object (instance)
s1 = Student("Arjun", 21)
s1.show_details()
