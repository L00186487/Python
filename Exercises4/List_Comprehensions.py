'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Demo For using a loop to populate a list
'''
# using a loop to populate a list
my_list = []
my_string = "Morning Folks!"
for letter in my_string:
    my_list.append(letter)

print(my_list)


# In a list comprehension, we collapse the block of code to below
my_string = "Morning Folks!"
my_list = [letter for letter in my_string]
print(my_list)

#  comprehension takes an element, for an element, from a string or other iterable object. 
my_list = [number for number in range(0,20)]
print(my_list)

# We can perform operations on variables, for example
my_list = [number * 10 for number in range(0,20)]
print(my_list)

# adding an if statement to further filter the output
my_list = [number * 10 for number in range(0,20) if number < 10]
print(my_list)

# I have a list of depths in feet on a US Sonar log file and 
# I want to convert them to meters, rounded to 2 decimal places.
conversion = 0.3048
my_depth_in_feet = [12.3, 13.8, 15.3, 12.1, 8.8]
my_depth_in_meters = [(round(depth * conversion, 2)) for depth in my_depth_in_feet] 
print(my_depth_in_meters)