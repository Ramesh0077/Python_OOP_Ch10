# 2. Difference Between Local and Instance Variables
# Inside a method, create both a local variable and an instance variable with the same name (course).
# Print both to see the difference.

class Class_variable:
    def __init__(self):
        self.course="Java"
    def dspaly(self):
        course="python"
        print(f"instance variable:{self.course}")
        print(f"local variable inside methods:{course}")
    

obj=Class_variable()
obj.dspaly()