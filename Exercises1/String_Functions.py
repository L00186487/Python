'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Demo String Functions

manipulating strings 
'''

a="Good Morning, MF\nWould you like Breakie?"
print(len(a))

my_string = "Almost finished now folks!"
my_upper = my_string.upper()
my_lower = my_string.lower()
print(f"Original: {my_string}")
print(f"Upper: {my_upper}")
print(f"Lower: {my_lower}")


text_with_spaces = "Michael Floyd  "
text_without_spaces = text_with_spaces.strip()
print(text_without_spaces)

text_with_brackets = "(Michael Floyd)"
text_without_brackets = text_with_brackets.strip('(')
text_without_brackets = text_without_brackets.strip('(')
print(text_without_brackets)