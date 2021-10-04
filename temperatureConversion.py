"""
Name:    temperatureConversion
Purpose: To convert temperature from Fahrenheit to Celcius.
Author:  Adam 
"""

degrees = int(input("Enter a temperature: "))

variable = str(input("Is the original temperature in 'C' or 'F'? "))

anotherTemperature = 'y'


if variable == 'F':
    degrees1 = degrees                
    degrees1 = (degrees - 32) * 5/9
    print("You entered", degrees, "in Fahrenheit degrees. This =", degrees1, "degrees Celcius.")

elif variable == 'C':
     degrees2 = degrees
     degrees2 = degrees * 9/5 + 32
     print("You entered", degrees, "in Celsius degrees. This =", degrees2, "degrees Fehrenheit.")

elif variable != 'F' or variable != 'C':
    print("You must enter either 'C' or 'F' !")
     
