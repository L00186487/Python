'''
Created By: Michael Floyd
Date: 25Nov23
Exercise: The Python Standard Library

It is better coding practice to import the specific function you require from a module, 
allowing the function to be directly accessed within your code. 
Do not use separate lines, for example, to import trigonometry functions use
'''

from math import sqrt
print("Input lengths of the two short triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse to four places is: {hypo:1.4f}".format(hypo=c))