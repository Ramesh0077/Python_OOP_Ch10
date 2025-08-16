# 10. Tracking Number of Objects
# Create a class with a class variable count starting at 0.
# Increment it in __init__ each time an object is created.
# Print total objects created.

class Tracking:
    count=0

    def __init__(self):
        Tracking.count+=1
        
    
track1=Tracking()
track2=Tracking()
track1=Tracking()
track2=Tracking()
track1=Tracking()
track2=Tracking()
print(f"Total objects created: {Tracking.count}")

