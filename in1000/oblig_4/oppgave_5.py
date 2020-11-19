# Create a new program in file oppgave_5.py
# This is a kind of notebook
# It has three modes: add the listing (name of person, phone number, sate of birth), list the items, remove, an item.


# This procedure contains main menu of the program
def main_menu():
    print('\nSimple notebook - Main menu: ')
    # We print the available functions
    print('1. Add items\n2. List items\n3. Remove items\n4. Quit')
    # User inputs the number of the menu item
    choice = int(input('Enter the menu item number to proceed or 4 to quit: '))
    # We check if its within the index range
    if choice <= len(actions) and choice >= 0:
        # We call the selected function from the list
        actions[choice - 1]()
    else:
        # Or print the warning and call the function recursively
        print('Your choice is out of range.')
        main_menu()


# This function let user add items to the notebook
def add_item():
    happy = False
    print('\nWe are going to add some items to your notebook.')
    # We enter the while loop and stay there until user enters 'q'
    while not happy:
        name = input('Please, enter a name (or "q" to quit to the main menu: ')
        if name != 'q':
            phone = input('Please, input the phone number: ')
            birthday = input('Please, input the birthdate: ')
            # The information provided by the user is then stored in a list, which in its trun is a value in
            # the dictionary
            listings_dict[name] = [phone, birthday]
        else:
            happy = True
    # We get back to the main menu
    main_menu()


# This procedure helps user remove items from the list
def remove_item():
    # Fist we check if there are any entries in the dictionary
    if len(listings_dict) > 0:
        happy = False
        print('These persons are in your notebook: ')
        # Then we print the stored names to remind them to the user
        for key in listings_dict:
            print(key)
        # We enter the while loop until user enters 'q'
        while not happy and len(listings_dict) > 0:
            rm_item = input('Please, enter a name to delete (or "q" to quit to the main menu: ')
            if rm_item != 'q':
                # We remove items from the dictionary by the key
                listings_dict.pop(rm_item)
            else:
                happy = True
        # We get back to the main menu
        main_menu()
    else:
        # If the notebook was empty we just get back to the main menu
        print('\nThe notebook is empty. We go back to main menu')
        main_menu()


# This procedure prints out the items
def print_items():
    # We check if the phonebook is not empty
    if len(listings_dict) > 0:
        # We print out its contents
        for key, value in listings_dict.items():
            print('{}\t\tPhone number: {p[0]}\t\tBirth date: {p[1]}'.format(key, p=value))
    else:
        # We print this if the notebook has no entries
        print('\nThe notebook is empty. We go back to main menu')
    # Back to main menu
    main_menu()


# This list stores the functions
actions = [add_item, print_items, remove_item, quit]

# We initiate an empty dictionary
listings_dict = {}

if __name__ == '__main__':
    # We start the program
    main_menu()
