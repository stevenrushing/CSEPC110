from math import pi

def area_of_square(length):
    return int(length) ** 2

def area_of_rectangle(length, height):
    return int(length) * int(height)

def area_of_circle(radius):
    return pi * (int(radius) ** 2)

side = input("What is the length of a side of the square? ")

print(f"The area of the square is {area_of_square(side):.4f}")

length = int(input("What is the length of the rectangle? "))
height = int(input("What is the height of the rectangle? "))

print(f"The area of the rectangle is {area_of_rectangle(length, height):.4f}")

radius = int(input("What is the radius of the circle? "))

print(f"The area of the circle is: {area_of_circle(radius):.4f}")