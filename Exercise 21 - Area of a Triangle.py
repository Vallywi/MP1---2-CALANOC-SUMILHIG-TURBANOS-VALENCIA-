# Exercise 21 - Area of a Triangle

length = input("Enter the length of the triangle: ")
height = input("Enter the height of the triangle: ")

def calculate_area(length, height):
    area = 0.5 * float(length) * float(height)
    return area

a = calculate_area(length, height)

print(f"The area of the triangle is: {a}square units ")
