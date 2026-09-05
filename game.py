import msvcrt
import time

# PizzaClicker99

while 1:

    time.sleep(0.01)

if msvcrt.khbit():
    key = msvcrt.getch()

if ord(key) == 32:
    print "Spacebar = Pressed"
