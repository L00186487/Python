'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Michael's Demo of Dictionaries

Dictionaries are unordered structures for storing objects. 
Dictionaries have a key pair format, uniquely identifying each entry, without needing to know its location. 
The format uses curly braces and is {“key1”:”value1”, “key2”:”value2”} 
'''

'''
In the below example, the keys() method is used to extract the keys of the dictionary. The list of keys are returned as a view object.
Here, dict_keys() is the view object and ['name', 'age', 'salary'] is the list of keys of the dictionary employee.
'''
employee = {'name': 'Phill', 'age': 22, 'salary': 3500.0}

# my_dictionary.keys() Method
# extracts the keys of the dictionary Example
dictionaryKeys = employee.keys()
print(dictionaryKeys)

# my_dictionary.values() Method
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales.values())

# my_dictionary.items() Method 
# Example: random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales.items())