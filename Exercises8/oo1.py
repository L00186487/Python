'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Demo Anatomy of a simple class

Simple Class by MF, by convention, use camel case to name classes
'''

# Create a class 
class MFzClass():
    
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for MFzClass")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)

my_class1 = MFzClass("Morning MF!")
my_class1.my_method()
print(type(my_class1))

my_class2 = MFzClass("How are you doing today?!")
my_class2.my_method()
print(type(my_class2))
