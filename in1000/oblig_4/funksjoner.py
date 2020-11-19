# This is a funciton that accepts two parameters (integers) and returns their sum
def adder(tall1, tall2):
    # We calculate and return sum
    return tall1 + tall2

# In this string we call the function two times and print the results out.
print('The sum of 1 and 2 is {}.\nThe sum of 21 and 21 is {}'.format(adder(1, 2), adder(21, 21)))


# This munction accepts to strings and counts the number of times the second string is a substring of the first string.
def tellForekomst(minTekst, minBokstav):
    # We count the substrings and return the result
    return minTekst.count(minBokstav)


# We ask the user to input the first string.
in_string_str = input('Enter a short text string now: ')
# We ask the user to enter the second string
in_letter_str = input('Enter one alphabetic character now: ')
# We pass the inputs to the function and assign the result to the variable.
count_2 = tellForekomst(in_string_str, in_letter_str)
# We print the result out.
print('The alphabetic character that you entered is found {} times in the string.'.format(count_2))
