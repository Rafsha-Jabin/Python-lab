PROGRAM:
class Student:
    # Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Method to display details
    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

    # Method for grading
    def grade(self):
        if self.marks >= 90:
            print("Grade: A")
        elif self.marks >= 75:
            print("Grade: B")
        elif self.marks >= 50:
            print("Grade: C")
        else:
            print("Grade: Fail")


# Creating object
s1 = Student("Rahul", 85)

# Calling methods
s1.display()
s1.grade()
