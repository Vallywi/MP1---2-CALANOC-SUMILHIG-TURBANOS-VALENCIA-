# Exercise 20 - Ideal Gas Law

pressure = float(input("Enter the pressure in Pa: "))
volume = float(input("Enter the volume in liters: "))
temperature = float(input("Enter the temperature in Kelvin: "))
R = 8.314
moles = (pressure * volume) / (R * temperature)
print(f"The number of moles is: {moles}m^3 ")
