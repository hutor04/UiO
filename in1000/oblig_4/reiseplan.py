# The program ask the user to input information. All in all there are 3 input lists with 5 items in each. The
# lists are then combined in one list.
# The user can choose an item from the list and the respective sublist.

# We initiate a new list
steder = []
# We ask user to input information (5 times)
for sted in range(5):
    plan = input('Print in the city, where you want to travel to: ')
    # A new item is added to the list
    steder.append(plan)

# We initiate a new list
klesplagg = []
# We ask user to input information (5 times)
for kles in range(5):
    clothing = input('Print the clothing you want to take with you: ')
    # A new item is added to the list
    klesplagg.append(clothing)

# We initiate a new list
avreisedatoer = []
# We ask user to input information (5 times)
for dato in range(5):
    # A new item is added to the list
    dates = input('Print the dates, when you want to travel: ')
    avreisedatoer.append(dates)

# We initiate a new list
reiseplan = []
# A new item is added to the list
reiseplan.append(steder)
# A new item is added to the list
reiseplan.append(klesplagg)
# A new item is added to the list
reiseplan.append(avreisedatoer)

# We print the contents of the list out
for i in reiseplan:
    print(i)

# We ask user for an index in the list
i1 = int(input('Select Destination - 0 or Clothing - 1, or Dates - 2: '))
# We check if the index is within the range
if i1 < len(reiseplan) and i1 >=0:
    # If the condition evaluates to true we ask for the second index
    i2 = int(input('Input the index of an item from the list you have just chosen: '))
    # We check if the index is within the range
    if i2 < len(reiseplan[i1]) and i2 >= 0:
        # If the condition evaluates to true we print the selected item
        print(reiseplan[i1][i2])
    else:
        # Print fail message
        print('Ugyldig input!')
else:
    # Print fail message
    print('Ugyldig input!')