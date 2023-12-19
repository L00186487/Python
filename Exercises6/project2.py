'''
Created By: Michael Floyd
Date: 25Nov23
Exercise: Demo packages

To help organize modules and provide a naming hierarchy, Python has the concept of packages. 
Packages are just collections of modules, and we normally keep them in a separate directory. 
I can build packages of reusable code, making all my work modular. To reuse this code in a different project, 
all I need to do is to copy the entire directory. Obviously, I need heavy commenting and comprehensible documentation to make this really work. 
'''

import mylib.cube as mycube
import mylib.square as mysquare

print(mycube.cube_text, mycube.cube(3))
print(mysquare.square_text, mysquare.square(3))