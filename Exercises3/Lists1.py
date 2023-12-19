'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Demo Lists
'''

my_list = [1,2,3,4,"A"]
a = len(my_list)
print(a)

slice_1 = my_list[1:3:1]
print(slice_1)

my_character = my_list[-1]
print(my_character)

'concatenate lists'
my_list_1 = [1,2,3,4,"A"]
my_list_2 = ["S", "T","FISH",9,10]
concatenated_list = my_list_1 + my_list_2
print(concatenated_list)

'Lists can also be nested'
my_list_1 = [1,2,3,4,"A"]
my_list_2 = ["S", "T","FISH",9,10]
concatenated_list = my_list_1, my_list_2
print(concatenated_list)

'lists are mutable, individual items may be indexed and selectively edited'
my_list_1 = ["S", "T","FISH",9,10]
print(my_list_1)
my_list_1[2] = "Chips"
print(my_list_1)

'Lists have a range of available methods, we can edit the list in place, appending items.'
my_list = ["one", "two", "three"]
print(my_list)
my_list.append("four")
print(my_list)

' take a string of data and create a list based on the contents of that string using comma.'
my_string = "12/9/22, 14.30, System Start, UB2204-Server"
list_of_values = my_string.split(",")
print(list_of_values)
