#!/usr/bin/env python3

"""Write a program to calculate the perimeter of a triangle"""

__author__="Lydia Frame"
__date__="01/25/2020"

#Prompt user to enter in the points of the triangle 
x_one = int(input("Enter x1: "))
print()
y_one = int(input("Enter y1: "))
print()
x_two = int(input("Enter x2: "))
print()
y_two = int(input("Enter y2: "))
print()
x_three = int(input("Enter x3: "))
print()
y_three = int(input("Enter y3: "))

#claculate distance between points 
distance_one = ((x_one - x_two)**2 + (y_one - y_two)**2)**0.5

distance_two = ((x_two - x_three)**2 + (y_two - y_three)**2)**0.5

distance_three = ((x_three - x_one)**2 + (y_three - y_one)**2)**0.5

#claculate perimeter 
perimeter = round(distance_one + distance_two + distance_three, 2)

#output perimeter
print("Perimeter is " + str(perimeter))
