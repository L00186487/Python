'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: I have an American air conditioner system returning temperatures, but I need the temperatures in standard units. 
Create a list of 10 values in degrees Kelvin. 
Write a code block to print these values in Celsius and Fahrenheit.
'''

degrees_kelvin = [300, 305, 308, 309, 310, 315, 316, 317, 318, 320]

for temp_kelvin in degrees_kelvin:
    # Convert Kelvin to Celsius
    temp_celsius = temp_kelvin - 273.15
    
    # Convert Celsius to Fahrenheit
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    
    print(f"Temperature in Kelvin: {temp_kelvin} K")
    print(f"Temperature in Celsius: {temp_celsius:.2f} °C")
    print(f"Temperature in Fahrenheit: {temp_fahrenheit:.2f} °F")
    

