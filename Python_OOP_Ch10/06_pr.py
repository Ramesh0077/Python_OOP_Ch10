# 6. Modify Instance Variables Dynamically
# Create a Laptop class with brand and price.
# Create an object and later update its price.
# Print before and after update.

class Laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

hp=Laptop("hp",344555)


# Print before update
print("Before update:")
print(f"Brand: {hp.brand}")
print(f"Price: ${hp.price}")
hp.price=4474
hp.brand="4uyh"
print("After update:")
print(f"Brand: {hp.brand}")
print(f"Price: ${hp.price}")

