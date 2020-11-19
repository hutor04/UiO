# The program asks user yes/no question and waits for the keyboard input.
# Valid answers are 'ja' and 'nei', we take care about capitalization.
# Once the program gets the input it evaluates it in the following way:
# if it gets 'ja' - it prints out 'Her har du en brus!', if it gets 'nei' -
# it prints out 'Den er grei.'
# If the input is invalid, the program prints out 'Det forstod jeg ikke helt.'

# Initiate a variable and wait for user's input
response = input('Kunne du tenke deg en brus? (Svar "ja" eller "nei"): ')
# Evaluate the input, make input lower case
if response.lower() == 'ja':
# Print if condition satisfied
    print('Her har du en brus!')
# Evaluate against 2nd condition, make input lower case
elif response.lower() == 'nei':
# Print if 2nd condition satisfied
    print('Den er grei.')
# Start 'else' part (none of conditions satisfied)
else:
# Print message if predefined conditions not satisfied
    print('Det forstod jeg ikke helt.')
