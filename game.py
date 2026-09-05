import msvcrt
import time

# PizzaClicker99

while 1:
    if msvcrt.kbhit():
        key = msvcrt.getch()

        if key == ' ':
            print "Spacebar = Pressed"
