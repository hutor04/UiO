# The program creates two variables that contain integers, sums them up
# with the result being stored in the third variable, and prints the sum out.
#
# Then the program creates two variables that contain strings, concatenates them,
# the result is saved to the variable named 'sammen' and printed out.
# 'sammen' variable is updated so that theres as space between the first
# two strings.

# Initiate variables with integer
a_int, b_int = 3, 5
# Print out variables one per line
print(a_int, b_int, sep='\n')
# Initiate new variable with the sum of 1st 2
sum_of_ab = a_int + b_int
# Print out the variable containing the sum
print('Sum:', sum_of_ab)
# Initiate variables with string
c_str, d_str  = 'San', 'Francisco'
# Print out variables one per line
print(c_str, d_str, sep='\n')
# Initiate variable with previous 2 variables concatenated
sammen = c_str + d_str
# Print out the variable
print(sammen)
# Update the variable, add space between strings
sammen = c_str + ' ' + d_str
# Print out the variable again
print(sammen)
