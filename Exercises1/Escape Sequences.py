'''''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Demo Escape Sequences
'''

print("Good Morning, MF")
print("Breakie ?")


'default value of the end parameter of the print function is \n, so a new line character is appended to the string.'
'We could supress this by following.'

print("Good Morning, MF", end = " ")
print("Breakie ?")   

'The following Includes an escape sequence \n to do a multi-line print command on one line of code'
print("Good Morning, MF\nWould you like Breakie?", )