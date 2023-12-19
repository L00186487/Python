'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Demo String Interpolation

Function to calculate the remaining endurance in minutes, 
checking and handling for divide by zero errors and for any value errors. 
'''

def calculate_remaining_endurance():
    while True:
        try:
            fuel_in_litres = int(input("Enter litres: "))
            fuel_consumption = int(input("Enter consumption: "))
            
            # Ensure fuel_consumption_rate is not zero to avoid division by zero
            if fuel_consumption == 0:
                raise ValueError("Flowmeter cannot calculate fuel flow with zero consumption rate")

            # Calculate remaining endurance in minutes
            remaining_endurance = fuel_in_litres / fuel_consumption
            return remaining_endurance

        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError:
            print("Error: Fuel consumption rate cannot be zero")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Continue
            print("This message shows every time, regardless of the program flow")

result = calculate_remaining_endurance()
print(f"Remaining Endurance: {result} minutes")
    