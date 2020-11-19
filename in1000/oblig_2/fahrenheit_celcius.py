# The program asks user to set the temperature in Fahrenheit. It accepts both
# integer and float values. The program prints the original value & then
# converts it to Celsius using the formula (temperature F) − 32) ∗ 5/9.
# The result is printed out.

# We initiate new variable with integer value and print it out.
temperature_f = 50

# Print the temperature in Celsiius
print('Temperature in Fahrenheit is set to {} F'.format(temperature_f))

# We create new variable. We assign the converted value to it
temperature_c = (temperature_f - 32)*5/9

# Print the resulting value in Celsius. It's a float with 2-digit precision
print('Temperature in Celsius is {:.2f} С'.format(temperature_c))

# Ask user to input temperature
temperature_f = float(input('Please, set the temperature in Fahrenheit: '))
# Print the provided value
print('You set the temperature to {} F.'.format(temperature_f))
#Perform the conversion
temperature_c = (temperature_f - 32)*5/9
# Print the resulting value in Celsius. It's a float with 2-digit precision
print('Temperature in Celsius is {:.2f} С'.format(temperature_c))
