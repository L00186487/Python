'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Demo String Interpolation

We can concatenate strings using + to give text and a variable.'
'''


a="would you like brekkie?"

print("Good Morning, MF " + a)



'''
In the old days, we used the .format() method. You define a string and place {} wherever you want to insert variables.
'''
a =5
b = 12
print("Good Morning, MF. For breakfast,would you like {}?".format("Fruit"))
print("We have {} apples, {} bananas and a total of {} pieces available.".format(a, b, a+b))


'''
Spell things out with keyword names
'''
a = "Good"
b = "MF"
c = "morning"
print("message is: {first}  {third}  {second}".format(first=a, second=c, third=b))


'''
provide the float as value:width.precision
'''
Number = 12345
Divisor = 333
Result = Number/Divisor
print("Result of {} divided by {} is {}".format(Number, Divisor, Result))
print("Limiting to a float with 4 decimal places would give {r:1.4f}".format(r=Result))

Number = 12345
Divisor = 333
Result = Number/Divisor
print(f"Result of {Number} divided by {Divisor} is {Result}")




