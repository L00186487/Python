'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Michael's Demo of Dictionaries

Dictionaries are unordered structures for storing objects. 
Dictionaries have a key pair format, uniquely identifying each entry, without needing to know its location. 
The format uses curly braces and is {“key1”:”value1”, “key2”:”value2”} 
'''

my_dictionary = {"FName":"Michael", "SName":"Floyd", "Occupation":"Footballer"}
print(my_dictionary)
print("Works as a " + my_dictionary["Occupation"])

'If I need the value of the key name, I retrieve it by key, not by its index. '
my_dictionary = {"FName":"Michael", "SName":"Floyd", "Occupation":"Footballer"}
print(my_dictionary)
my_dictionary["Salary"] = "Not Enough!"
print(my_dictionary)


# Create the initial Dictionary
my_dictionary = {"FName":"Michael", "SName":"Floyd", "Occupation":"Soccer Footballer"}
print(my_dictionary)
# Add a Key:value pair
my_dictionary["Salary"] = "Not Enough!"
print(my_dictionary)
# Edit one value
my_dictionary["Occupation"] = "GAA Footballer!"
print(my_dictionary)

