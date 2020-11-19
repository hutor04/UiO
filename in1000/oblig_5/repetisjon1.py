# This program asks the user to input values, it then concatenates them and store in a list.
# There are three options: proceed with entry, print data, and exit

# Data storage
mineOrd = []


# The function concatenates two strings.
def slaaSammen(streng1, streng2):
    return streng1 + streng2


# The function prints out the content of a list.
def skrivUt(input_list):
    for i in input_list:
        print(i)

# The flag
happy = False

# We start the loop and continue until the flag changes its state.
while not happy:
    # Menu
    ask_input = input('Type in "i" to input two strings and concatenate them,\n'
                      'type in "u" to print out what we have in memory,\n'
                      'type in "s" to exit the program: ')
    # Check if it's first menu item
    if ask_input == 'i':
        # Ask for the input
        str1 = input('Input the first string: ')
        str2 = input('Input the second string: ')
        # Append concatenated strings to the list.
        mineOrd.append(slaaSammen(str1, str2))
    # Check if it's second item
    elif ask_input == 'u':
        # Print out the content of the list.
        skrivUt(mineOrd)
    # Check if user wants to exit.
    elif ask_input == 's':
        # Change the flag state.
        happy = True

