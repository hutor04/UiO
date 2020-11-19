# The program asks user yes/no question and waits for the keyboard input.
# Valid answers are 'ja' and 'nei'. Once the program gets the input
# evaluates it in the following way:
# if it gets 'ja' - it prints out 'Her har du en brus!', if it gets 'nei' -
# it prints out 'Den er grei.'
# If the input is invalid, the program prints out 'Det forstod jeg ikke helt.'


# Initiate a variable and wait for user's input
response = input('Kunne du tenke deg en brus? (Svar "ja" eller "nei"): ')

if response == 'ja':						# Evaluate the input
    print('Her har du en brus!')			# Print if condition satisfied
elif response == 'nei':						# Evaluate against 2nd condition
    print('Den er grei.')					# Print if 2nd condition satisfied
else:										# Start 'else' part (none of conditions satisfied)
    print('Det forstod jeg ikke helt.')		# Print message if predefined conditions not satisfied
