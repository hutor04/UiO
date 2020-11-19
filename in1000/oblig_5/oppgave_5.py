# Create a program that reads a file that contains a name of the boxing fighter followed by his statistics.
# Acceptable file format:
# ALPHABETIC AND SPACES
# 1 to N ALPHABETIC INT
# The program should then store the data in the dictionary, where the key is the name of the boxer, and the
# statistics are stored as the list.
# The program should then print out the data in a well-structured way.

import os.path

# The settings
FILE_NAME = 'oppgave_5.txt'
DATA_DICT = {}


# We check if the input file is in place, and we can proceed.
def check_file(f_name):
    happy = False
    if os.path.isfile(f_name):
        print('Input file is ready, we can proceed.')
        happy = True
    else:
        print('Input file is not found. Check settings')
    return happy


# This function reads data from file and returns the generator object. This approach helps us
# to deal with potentially large files, and avoid memory overflow.
def file_reader(filename):
    with open(filename, 'r') as file:
        for line in file:
            # Yield line and strip new line characters
            yield line.strip()


# This is the parser function. It evaluates each line and updates DATA_DICT. It can return the number of
# entries it parsed. May be useful to check data integrity.
def parser(gen_object):
    # Counter
    counter = 0
    # Temporary dictionary key
    tmp_key = ''
    # Temporary dictionary value
    tmp_value = []
    # We start looping over the generator
    for line in gen_object:
        # We search for the beacon line. It should contain only alphabetical characters.
        if all([x.isalpha() for x in line.split()]):
            # We reset the temporary key
            tmp_key = line
            # We reset the temporary value
            tmp_value = []
            # Increment counter
            counter += 1
        else:
            # If the line is not a beacon line we split it once from the right side
            tmp_value.append(line.rsplit(maxsplit=1))
        # Update the dictionary
        DATA_DICT[tmp_key] = tmp_value
    return counter


# This function prints out the contents of the dictionary.
def check_data(data_dict):
    for key, value in data_dict.items():
        print('\n{}'.format(key))
        for item in value:
            print('    {p[0]}: {p[1]}'.format(p=item))


if __name__ == '__main__':
    if check_file(FILE_NAME):
        reader = file_reader(FILE_NAME)
        parser(reader)
        check_data(DATA_DICT)
