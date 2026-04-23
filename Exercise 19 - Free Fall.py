# Exercise 19 - Free Fall

GRAVITY = 9.8
INITIAL_VELOCITY = 0
d_meter = float(input("Enter the height from which the object is dropped (in meters): "))

def calculate_final_velocity(d_meter):
    final_velocity = (2 * GRAVITY * d_meter)**0.5
    return final_velocity

vF = calculate_final_velocity(d_meter)

print(f"The final velocity is {vF} m/s")
