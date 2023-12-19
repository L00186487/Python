'''
Created By: Michael Floyd
Date: 25Nov23
Exercise: The Python Standard Library

The import statement does not make the contents of a module directly accessible. 
Instead, it creates a namespace, making the contents available. 
In this case the function sqrt becomes available as part of the math package.
'''

import math
print("Input lengths of the two short triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = math.sqrt(a**2 + b**2)
print("The length of the hypotenuse to four places is: {hypo:1.4f}".format(hypo=c))