'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Demo For While Loops
'''

# While loops will continue to execute a block of code so long as the condition is true. 
x = 0
while x < 10:
    print(f"X is = {x}")
    x = x + 1
else:
    print(f"As x is now = {x}, we are all finished")


# Sometimes I want a program to run forever. 
# I can do this by enclosing the code in a never-ending while block, using while True: or while 1:
print("press [ctrl][c] to exit")
while 1:
    pass

