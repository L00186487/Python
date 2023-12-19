'''''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Demo examples using slicing
'''

'extract characters from the string  in the format [start:stop:step].'
a = "Greetings!"
print(a[0:4:1])

'use forward or reverse indexing'
a = "Greetings!"
print(a[-1:-5:-1])

' Grab a single character'
a = "Greetings!"
print(a[5])

'slice the string and reassemble a new string with changes'
a = "michael"
first_letters = a[0:2:1]
last_letter = a[-1]
insert_letter = "a"
b = first_letters + insert_letter + last_letter
print(b)


'You cannot add a string and a number, they are different types. Examine the code below.'
first_character = "p"
second_character = "4"
a = first_character + second_character
print(a)


first_number = 1
second_number = 2
a = first_number + second_number
print(a)