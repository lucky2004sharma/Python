class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_details(self):
        print("----- Student Details -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# Creating object
student1 = Student("Rahul", 20, "Python")

# Calling method
student1.show_details()