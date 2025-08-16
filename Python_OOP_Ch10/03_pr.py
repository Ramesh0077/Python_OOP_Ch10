# 3. Class vs Instance Variable
# Create a Car class with a class variable wheels = 4.
# Create two cars and change wheels for one object.
# See if it affects the other object.
class Car:
    wheels=4
car1=Car()
car1.wheels=6
car2=Car()
print(car1.wheels)
print(car2.wheels)