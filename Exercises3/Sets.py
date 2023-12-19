'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Michael's Demo of Sets

Sets are an unordered collection of unique objects. 
Typical methods are add() which will take only one argument at a time. 
In the example below, no error is raised when I try to add the number 2 a second time, 
the set is a collection of unique objects, the add is ignored.
'''

my_set = set()
print(type(my_set))
print(my_set)

my_set.add(1)
my_set.add(2)
my_set.add(2)
print(my_set)
