# 8. Object Interaction
# Create a Person class with name and a method greet(other_person) that prints:
# Hello <other_person.name>, I am <self.name>
# Create two objects and make them greet each other.

class Person:
    
    def __init__(self,name):
        self.name=name
    def greet(self,other_person):
        print(f"Hello {other_person.name}, I am {self.name}")
    
person1=Person("Ram")
person2=Person("Krishna")
person1.greet(person2)
person2.greet(person1)
