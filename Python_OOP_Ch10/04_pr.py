# 4. Using @staticmethod
# Create a MathHelper class with a static method square(number).
# Call it using both the class name and an object.

class MathHelper:
    @staticmethod
    def square(number):
        rresult= number*number
        print(rresult)
obj=MathHelper()
obj.square(4)
MathHelper.square(3)
