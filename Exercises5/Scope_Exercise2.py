'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Demo Scope
'''

'''
find_num function check if a number exists in the number_list. 
If the number is not found in the list, the function returns None
'''

def find_num(number_list: list, number: int)->bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
            pass

result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)


# Function adjusted to returned False instead of None. Removed else
def find_num(number_list: list, number: int) ->bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
    return False

result = find_num([1, 2, 3, 4, 5, 6, 7, 8], 9)
print(result)


# Function adjusted to returned True. 9 is added to list
def find_num(number_list: list, number: int) ->bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
    return False

result = find_num([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
print(result)

