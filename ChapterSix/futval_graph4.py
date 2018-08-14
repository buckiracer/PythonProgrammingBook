# futval_graph4.py

from graphics import *

def createLabeledWindow():
    window = GraphWin("Investment Growth Chart", 320, 240)
    window.setBackground("white")
    window.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1,0),' 0.0K').draw(window)
    Text(Point(-1,2500),' 2.5K').draw(window)
    Text(Point(-1,5000),' 5.0K').draw(window)
    Text(Point(-1,7500),' 7.5K').draw(window)
    Text(Point(-1,10000),' 10.0K').draw(window)
    return window    

def drawBar(window, year, height):
    # Draw a bar in window starting at year with given height
    bar = Rectangle(Point(year,0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

def main():
    # Introduction
    print("This program plots the growth of a 10-year investment.")

    # Get principal and interest rate
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))
    # Create a graphics window with labels on left edge
    win = createLabeledWindow()

    drawBar(win,0,principal)
    for year in range(1,11):
        principal = principal * (1 + apr)
        drawBar(win, year, principal)

    input("Press <Enter> to quit.")
    win.close()
main()
    