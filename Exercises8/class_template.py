"""
Class template by MF

Revision History
12DEC23: Alpha

This is a basic template for a class named MyTemplate with a constructor (__init__ method) to initialize attributes, 
and a method that demonstrate how to define and use methods within a class. 
"""

#Template Class that contains two methods which can be reused when required in other programs
class MyTemplate:
    def __init__(self, attribute1, attribute2):        #Constructor method.Initializes the object when it is created.
        self.attribute1 = attribute1                   # Assign the values passed to the constructor to attributes of the class
        self.attribute2 = attribute2

    def method1(self):                                 #Method named method1 within the class. 
        print(f"Method 1 called with attributes: {self.attribute1}, {self.attribute2}")


if __name__ == "__main__":
    # Create an instance of the class
    my_instance = MyTemplate("Michael", "Floyd")

    # Print attributes
    print(f"Attribute 1: {my_instance.attribute1}")
    print(f"Attribute 2: {my_instance.attribute2}")

    # Call method
    my_instance.method1()
 