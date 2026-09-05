import msvcrt
import time

# PizzaClicker99

Score = 0

def mainmenu():
    print "=======MAIN======="
    print "| 1. Launch Game  |"
    print "| 2. My Website   |"
    print "| 3.    Exit      |"
    print "==================="
    
while 1:

if msvcrt.khbit():
    key = msvcrt.getch()
    if ord(key) == 32:
        print "Spacebar = Pressed"
        score +1
        print score
        sys.exit(0)
