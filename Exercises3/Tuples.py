'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Demo Tuples

Tuples are like lists, but immutable. Once an element has been assigned to a tuple, it cannot be changed. 
Tuples are defined by regular brackets.
'''

my_list = ["one", "two", "three"]
my_tuple = ("one", "two", "three")
print(type(my_list))
print(type(my_tuple))

' standard methods like count() and index(). can be used with tuples'
my_tuple = ("one", "two", "three", "one")
# How many times does "one" appear in the tuple
print(my_tuple.count("one"))
# At what position in the tuple can i first find "one"
print(my_tuple.index("one"))

