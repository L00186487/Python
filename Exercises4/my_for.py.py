

iterable_variable = [1,2,3,4,5,6]

for item in iterable_variable:
    # For each item, execute this code block
    print(item)

# print out odd number only
iterable_variable = [1,2,3,4,5,6]

for item in iterable_variable:
    if item %2 != 0:
        print(item)

# print out even number only
iterable_variable = [1,2,3,4,5,6]

for item in iterable_variable:
    if item %2 == 0:
        print(item)


# add each number in the list
iterable_variable = [1,2,3,4,5,6]
total = 0

for item in iterable_variable:
    total = total + item

print(total)


# Define a string to iterate over
for this_letter in "Michael Floyd":
    # Specify which letter to test for
    if this_letter == "M":
        # Found the test letter
        print(f"Woo hoo, found a {this_letter}!")
        # Exit the current loop
        break
    else:
        # Didn't find the test letter
        print(f"Aww man, I didn't want a {this_letter}!")


my_list = [1,2,3,0]

for my_number in my_list:
    if my_number == 1:
        pass  # Does nothing, just Moves to next iteration
    if my_number == 2:
        continue
    if my_number == 3:
        print(f"Found the number {my_number}")
    if my_number == 0:
        break

 # iterate through any sequence, for example a tuple. We can also nest tuples in lists, etc. 
list_of_tuples = [(1,2), (3,4), ("A", "B")]
for item in list_of_tuples:
    print(item)  

# Tuple unpacking
list_of_tuples = [(1,2), (3,4), ("A", "B")]
for a,b in list_of_tuples:
    print(a)  
    print(b)

# for loop in Python that iterates over a range of numbers. 
# The range(1, 100, 5) generates a sequence of numbers starting from 1, 
# incrementing by 5 in each step, and stopping before reaching 100
for index in range(1, 100, 5):
    print(index)