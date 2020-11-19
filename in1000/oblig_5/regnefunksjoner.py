# This file includes functions that perform various calculations


# The function takes two arguments and returns their sum
def addisjon(x, y):
    return x + y

# This is the test of the function
print('\nTest addition with inputs -1 and -3. Result: {}.'.format(addisjon(-1, -3)))


# The function takes two arguments and performs substruction
def substraksjon(x, y):
    return x - y

# Assert statements to test the function
assert substraksjon(10, 8) == 2
assert substraksjon(-11, -10) == -1
assert substraksjon(256, -111) == 367


# The function takes two arguments and performs devision
def divisjon(x, y):
    return x / y

# Assert statements to test the function
assert divisjon(10, 5) == 2
assert divisjon(-15, -10) == 1.5
assert divisjon(11, -3) == -3.6666666666666665


# The function takes one argument and performs the conversion to from inches to cm
def tommerTilCm(antallTommer):
    # We test if the argument is more than 0
    assert antallTommer > 0
    return antallTommer * 2.54

print('Test conversion from inches to cm with input 11. Result: {}'.format(tommerTilCm(11)))


# This is a routine procedure that asks for the input and call the previously defined functions.
def skrivBeregninger():
    print('\nUtregninger:')
    tall1 = float(input('Skriv inn tall 1: '))
    tall2 = float(input('Skriv inn tall 2: '))

    print('\nResultat av summering: {}'.format(addisjon(tall1, tall2)))
    print('Resultat av substraksjon: {}'.format(substraksjon(tall1, tall2)))
    print('Resultat av divisjon: {}'.format(divisjon(tall1, tall2)))

    print('\nKonvertering fra tommer til cm:')
    tall3 = float(input('Skriv inn et tall: '))
    print('Resultat: {}'.format(tommerTilCm(tall3)))

# We call the routine
skrivBeregninger()
