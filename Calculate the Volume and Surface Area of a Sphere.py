# Assigment no 3 ::: Get input from user and calculate the area of a triangle

import math

def calculate_sphere():
    radius = float(input("Enter the radius of the sphere: "))
    volume = (4/3) * math.pi * radius ** 3
    surface_area = 4 * math.pi * radius ** 2
    return (volume, surface_area)

volume, surface_area = calculate_sphere()
print(f"For a sphere with radius {radius}, the volume is {volume} and the surface area is {surface_area}.")