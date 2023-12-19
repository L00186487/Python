'''
Created By: Michael Floyd
Date: 25Nov23
Exercise: The Python Standard Library

It is better coding practice to import the specific function you require from a module, 
allowing the function to be directly accessed within your code. 
Do not use separate lines, for example, to import trigonometry functions use
'''

cube_text = "Yo, time to cube stuff!"

def cube(x):
    return x*x*x

# Uncomment to test
# print(cube(2))

if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
else:
    print(f"This module is called {__name__} and is being called by another script")