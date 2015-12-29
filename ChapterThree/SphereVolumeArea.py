# SphereVolumeArea.py
# Simple program to calculate the volume and surface area of speher
# Input is radius

import math

def main():
    radius = eval(input("Please input the radius of the sphere: "))
    volume = 4 / 3 * math.pi * radius ** 3
    area = 4 * math.pi * radius ** 2

    print("The sphere has a volume of: ", volume, "and area of: ", area)

main()
