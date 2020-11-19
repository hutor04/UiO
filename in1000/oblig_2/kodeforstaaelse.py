# 1. The code contains error.
# It attempts to concatenate values of incompatable types.
# b is an integer and 'Hei!' is a string.
# 2. If you run the code when b is less than 10, the interpreter will throw
# 'unsupported operand type' exception.
# 3. Additionally, if the user inputs values that are not integers, the program
# will through invalid literal error. We should handle this issue via catching
# the exception or test if all the characters in the input are integers before
# we make the conversion.
# 4. Another problem is that this bug will cause the exception only if the user
# inputs the value below 10. It means that the error may persist in the code
# for a while.

# User inputs value
a = input("Tast inn et heltall! ")
# We convert the string to integer
b = int(a)
# We check if the value is less than 10
if b < 10:
# If the condition is satisfied the program crashes here because operands are
# of unsupported types.
# If we want to fix it, we should change it to print(str(b) + 'Hei!')
    print(b + "Hei!")
