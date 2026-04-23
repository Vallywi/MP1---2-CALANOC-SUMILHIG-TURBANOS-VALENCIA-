# Exercise 22 - Area of a Triangle (Again)

first_side = float(input("Enter the length of the first side of the triangle: "))
second_side = float(input("Enter the length of the second side of the triangle: "))
third_side = float(input("Enter the length of the third side of the triangle: "))
s = (first_side + second_side + third_side) / 2

def calculate_area(first_side, second_side, third_side):
    area = (s * (s - first_side) * (s - second_side) * (s - third_side)) ** 0.5
    return area

totalArea = calculate_area(first_side, second_side, third_side)

print(f"The area of the triangle is: {totalArea} ")
