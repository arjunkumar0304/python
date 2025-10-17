class Student:
    def set_details(self, name, age, grade):

        self.name = name
        self.age = age
        self.grade = grade


    def display_info(self):
        # Display the student's details
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


# List to store all students
students = []

for i in range(5):
    print(f"Enter details for student {i + 1}:")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")

    # Create a Student object and set detail
    student = Student()
    student.set_details(name, age, grade)
    students.append(student)

# Display details of all students
print("\nAll Student Details:")
for student in students:
    student.display_info()
