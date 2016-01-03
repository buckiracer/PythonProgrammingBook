# Click.py
# Simple program to demonstrate mouse click in window interaction

from graphics import *

def main():
    win = GraphWin("Click Me!")
    for i in range (10):
        p = win.getMouse()
        print("You clicked at: ", p.getX(), p.getY())

    win.close()

main()

