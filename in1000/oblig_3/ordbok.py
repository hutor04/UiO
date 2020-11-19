# The program initiates a dictionary with product names as keys and their prices as values. It then prints out the list
# Then the program asks the user to input a new product and its price two times.
# It ads new products to the dictionary and then prints a new dictionary.

# We create a dictionary that holds product names as keys and their prices as values.
products = {'melk': 14.90, 'brød': 24.90, 'yoghurt': 12.90, 'pizza': 39.90}
# We print the dictionary
print(products)

# We enter the for-loop with two repetitions.
for i in range(2):
    # We ask for a product name
    product = input('Please, provide the name of a product: ')
    # We are going to handle the exception that rises if the user inputs not a number on the next step
    try:
        # We ask the user to enter the price
        price = float(input('Provide the price of the product (digits , please): '))
        # We then ad a new product to the dictionary
        products[product] = price
    except ValueError:
        # We print this if the user enters price with alphabetic characters. And we don't add this value to the list.
        print('We expected a digit here.')
# We print the list again
print(products)
