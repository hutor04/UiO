# Test the class Hund

from hund import Hund


def hovedprogram():
    h = Hund(5, 10, 10)
    print('The dog is jumping.')
    for i in range(7):
        h.spring()
        print("The dog's weight is {}.".format(h.vekt))
    print('The dog is eating.')
    for i in range(7):
        h.spis(i)
        print("The dog's weight is {}.".format(h.vekt))


if __name__ == '__main__':
    hovedprogram()