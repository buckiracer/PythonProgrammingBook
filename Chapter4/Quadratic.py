# Quadratic.py
# A simple program that computes the real roots of a quadratic equation
# Illustrates the use of the 'math' library
# Note. This program crashes if the equation has no real roots

import math     # makes the math library available

def main():
    print("This program finds the real solution to a quadratic")
    print()

    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print("The solutions are: ", root1, root2)

main()

