'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: 
Write a function to search for an even number in a list of numbers. 
Return True if you find an even number. 
Return False if you do not. 

'''
#The function iterates through the numbers and returns True as soon as it finds an even number. 
# If no even number is found, it returns False.
# returns true when it reaches 8

def even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            return True
    return False


numbers_list = [1, 3, 5, 7, 8, 9]
result = even_numbers(numbers_list)
print(result) 


'Write a lambda function to calculate the volume of a cylinder.'

# This line defines a lambda function named cylinder_volume. This lambda function takes two parameters, radius and height, 
# and calculates the volume of a cylinder using below formula 

cylinder_volume = lambda radius, height: 3.14 * radius**2 * height

# Assigning values to the variables radius and height.
radius = 5
height = 5
# call Lambda function:
result = cylinder_volume(radius, height)
print(result)  