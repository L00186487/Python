'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Demo Scope
'''
# Divisible function checks whether the numerator is divisible by the denominator. 
# It uses (%) to calculate the remainder when numerator is divided by denominator, 
# numerator and demoninator are type int variables
# Bool returns True if the remainder is zero, indicating divisibility, and False otherwise.
def divisible(numerator: int, denominator: int)->bool:
    return numerator % denominator == 0

# Will return true when no remainder and divides equally
print(divisible(30,5))

