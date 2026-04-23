# Exercise 18 - Volume of a Cylinder

import math

radius = input("Enter the radius in cm: ")
height = input("Enter the height in cm: ")

def calculate_volume(radius, height):
    volume = math.pi * (float(radius) ** 2) * float(height)
    return volume

v = calculate_volume(radius, height)

print(f"The volume of the cylinder is: {v}m^3 ")

