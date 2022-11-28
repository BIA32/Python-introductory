temperature = float(input("Enter the temperature in celsius and it will convert into Kelvin, and Fahrenheit: "))

fahrenheit = 1.8 * temperature + 32
kelvin = 273.15 + temperature

print('%0.3f Celsius = %0.3f Fahrenheit.' % (temperature, fahrenheit))
print('%0.3f Celsius = %0.3f Kelvin.' % (temperature, kelvin))