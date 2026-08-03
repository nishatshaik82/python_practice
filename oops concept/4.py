#create a person class and drive students and teacher

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def display_info(self):
        print("Student Name:", self.name)
        print("Age:", self.age)

class Teacher(Person):
    def display_info(self):
        print("Teacher Name:", self.name)
        print("Age:", self.age)

student = Student("Rahul", 20)
teacher = Teacher("Anitha", 35)

student.display_info()
teacher.display_info()