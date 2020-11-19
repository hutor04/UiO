# This program reads data from file and performs operations on the data.


# The file reader. Reads the file and return the dictionary.
def innlesing(filnavn):
    data_dict = {}
    with open(filnavn, 'r') as input_file:
        for line in input_file:
            line_lst = line.rsplit(maxsplit=1)
            data_dict[line_lst[0]] = int(line_lst[1].strip())
    return data_dict


# The function sorts the dictionary by values and prints out the information about the item
# with the highest value.
def maanedensSalgsperson(data_dict):
    data_dict_sorted = sorted(data_dict.items(), key=lambda x: x[1])
    print('Maanedens ansatte er {p[0]} med {p[1]} salg.'.format(p=data_dict_sorted[-1]))


# The function return sum of the values in the dicitonary
def totaltAntallSalg(data_dict):
    return sum([val for val in data_dict.values()])


# The function calculates the average all the values in the dictionary
def gjennomsnittSalg(data_dict):
    avg_float = totaltAntallSalg(data_dict) / len(data_dict)
    return round(avg_float, 2)

# The main routine.
def hovedprogram():
    data = innlesing('salgstall.txt')
    maanedensSalgsperson(data)
    print('\nAktive selgere denne maaneden: {}'.format(len(data)))
    print('Totalt antall salg: {}'.format(totaltAntallSalg(data)))
    print('Gjennomsnittlig antall salg per salgsperson: {}'.format(gjennomsnittSalg(data)))


if __name__ == '__main__':
    hovedprogram()
