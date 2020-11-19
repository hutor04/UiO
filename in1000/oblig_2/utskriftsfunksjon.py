# The program consists of two parts. First - procedure that requests keyboard
# input and prints out the formated string. Second - the for-loop that calls
# the procedure three times.

# Initiate function
def info_request():
# Ask for the name of the user
    u_name_str = input('Hva heter du? ')
# Ask for the place they live
    u_address_str = input('Hvor kommer du fra? ')
# Print out the obtained information in the formatted string
    print('Hei, {}! Jeg vet du er fra {}.\n'.format(u_name_str, u_address_str))

# We enter the for-loop and set it to repeat three times
for i in range(3):
# We call the function
    info_request()
