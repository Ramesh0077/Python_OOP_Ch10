# 1. Create and Access Instance Variables
# Create a Student class with name and marks.
# Use __init__ to initialize them.
# Create two students and print their details.

class Student:
   
    def __init__(self,name,marks):
        self.name=name 
        self.marks=marks
        print(f"Marks:{marks}")
        print(f"name:{name}")

    def sum(self):
        print("Simple method")
        


Student1=Student("ramesh",900)
Student2=Student("djjf",74874)
Student2.sum()