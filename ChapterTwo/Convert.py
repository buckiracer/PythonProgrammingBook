# Convert.py
# A simple program to convert Celcius to Fahrenheit 
# By W.Gross


def main():

    print("This program will convert user entered")
    print("degrees Celsius to Fahrenheit\n")

    for temps in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9 / 5 * celsius + 32
        print("The temperature is ", fahrenheit, "degrees Fahrenheit")

    for temperature in range(11):
        fahrenheit = 9/5 * (temperature*10) + 32
        print(temperature,"degrees Celsius is ", fahrenheit, "degrees Fahrenheit")

main()