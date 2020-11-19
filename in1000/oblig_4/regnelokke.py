# We ask the user to enter numbers. 0 stops the input.
# This is a flag, we use it to exit the while-loop.
happy = 0
# We initiate an empty list, where we will store user input.
in_numbers = []
# We initiate the while loop over here.
while not happy:
    # We ask for the input
    a = int(input('Print a digit (only). Print 0 to exit: '))
    # Check if the input is not 0
    if a != 0:
        # If the condition evaluates to True, we add the number to the list.
        in_numbers.append(a)
    # Else we exit while loop here.
    else:
        happy = 1

# We loop throught the list and print each element
for element in in_numbers:
    print(element)

# We initiate the variable minSum with 0.
minSum = 0
# We loop over each element in the list and add them up to minSum
for element in in_numbers:
    # Addition
    minSum += element
print('The sum of numbers you entered is {}.'.format(minSum))

# This finds the minimal value.
# We set the minimal value as the first element of the list
min_element = in_numbers[0]
# Then we loop through each element of the list
for element in in_numbers:
    # And compare it with the minial value. If the element is less than minimal value it replaces it.
    if element < min_element:
        min_element = element
# We print the result
print('The minimal number is {}.'.format(min_element))


# This finds the maximal value.
# We set the maximal value as the first element of the list
max_element = in_numbers[0]
# Then we loop through each element of the list
for element in in_numbers:
    # And compare it with the minial value. If the element is more than maximal value it replaces it.
    if element > max_element:
        max_element = element
# We print the result
print('The maximal number is {}'.format(max_element))
