# SlopeDistance.py
# Simple program that takes to (x,y) points as input
# Calculates the slope and distance between these two points

import math

def main():
    x1, y1 = eval(input("Please enter the x,y coordinate of point 1: "))
    x2, y2 = eval(input("Please enter the x,y coordinate of point 2: "))

    slope = (y2 - y1) / (x2 - x1)

    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    print("The slope between the two points is: ", slope, "at a distance of: ", distance)

main()

