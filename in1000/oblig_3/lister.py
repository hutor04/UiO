# The program creates a list with three numbers. We then append another number to the list and print out the first and
# the third elements of the list.
# The program asks the user to provide four names via keyboard input. The names are appended to a new list.
# The program then checks if a certain string is present in the list and prints out different messages based of the
# outcome.

# We create a list with three elements
my_list = [1, 2, 3]
#  We append a new item to the list
my_list.append(4)
# We print the first and the third elements from the list.
print('{d[0]} {d[2]}'.format(d=my_list))

# This variable holds the name to be checked (my name).
MY_NAME = 'Yauhen'
# We initiate an empty list.
names = []
# We enter the for loop to ask for the user input for four times.
for i in range(4):
    # We get user input and store it to a variable
    temp_name_string = input('Give me a name: ')
    # We make the input title case and append the variable to the list of names
    names.append(temp_name_string.title())
# We check if check-name is in the list
if MY_NAME in names:
    # If the condition evaluates to true we print this message
    print('Du husket meg!')
# If the check fails we print another message.
else:
    print('Glemte du meg?')

# We create a new list that is a concatenation of two lists
two_lists = my_list + names
# We then print a new list
print(two_lists)
# We delete two last items in the list using the slice notation
two_lists[-2:] = ''
# We print the updated list
print(two_lists)
