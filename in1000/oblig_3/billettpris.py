# The program contains a procedure that that asks a user their age. It then determines the price of the ticket
# based on the age that user inputs.


def determine_price():
    alder = int(input('Hei, will you tell me how old are you? '))
    billettpris = 0
    if alder <= 17:
        billettpris = 30
    elif alder >= 63:
        billettpris = 35
    else:
        billettpris = 50
    print('The price of your ticket is {} Kr.'.format(billettpris))

for i in range(4):
    determine_price()

# 1. The procedure does not check if user inputs numbers or alphabetic characters.
# 2. The user may enter invalid age e.g. negative or too high.
# 3. The code is hard to maintain if the price of the tickets changes or if we change the price policy for different
#    ages. We have 'magic' numbers all over the procedure.
