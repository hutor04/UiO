# This program reads temperature reading from a file one per line and calculates their average.

# We read data from file to this list
temperature_lst = []

# We use file context manager to open the file.
with open('temperatur.txt', 'r') as in_file:
    # We loop through each line from file
    for line in in_file:
        # We strip newline characters from each line and convert it to integers and then add them
        # to the list
        temperature_lst.append(int(line.rstrip()))


# We define the function
def avg_temperature(temp_values_lst):
    # This variable will hold sum of all values in list
    temp_sum = 0
    # We loop through values and sum them
    for i in temp_values_lst:
        temp_sum += i
    # We return sum devided by the number of elements in list
    return temp_sum / len(temp_values_lst)

print('\nThe average temperature is {}.'.format(avg_temperature(temperature_lst)))