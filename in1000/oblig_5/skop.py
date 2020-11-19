a = 1
def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)


def hovedprogram():
    #a = 42
    b = 0
    #print(b)
    b = a
    #a = minFunksjon()
    #print(b)
    print(b)
    return 'aaa'

hovedprogram()

# First, we define the function minFunksjon. minFunksjon does not take any arguments. minFunksjon loops
# though range from 0 till 2 (exclusive), i.e. two times. For each cycle it attempts to do the following:
# Assign value 2 to variable 'c'.
# Assign value ('c' + 1) to variable 'c'.
# Assign value 10 to variable 'b'.
# Assign value ('b' + 'a') to variable 'b'. There is a problem here, because the variable 'a' is not
# available within the current scope. The execution of function minFunksjon as it is will cause
# the program to crash.
# Print variable 'b'. Will not be executed due to the exception.
# The function will not a return any value due to the exception.

# Second, we define the procedure hovedprogram.
# It does the following:
# Assign value 42 to variable 'a'
# Assign value 0 to variable 'b'
# Print content of variable 'b' (it's 0)
# Assign value of variable 'a' to 'b'
# Assign value returned by function minFunksjon to 'a'. The execution will raise exception here,
# becase the minFunksjon will raise an exception.
# Printing of 'b' and 'a' will not be executed.

# hovedprogram() calls the procedure 'hovedprogram' and starts its execution.