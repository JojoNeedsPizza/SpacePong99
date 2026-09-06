import msvcrt
import time
import sys

# PizzaClicker99

Score = 0
pos = 20
spielfeldbreite = 45
leistenbreite = 5

def mainmenu():
 print "=======MAIN======="
 print "| 1. Launch Game |"
 print "| 2. My Website  |"
 print "| 3.    Exit     |"
 print "=================="

 mainmenuinput = raw_input("Enter a Number from 1 - 3")


while 1:
 
 leerlinks = " " * pos
 leerrechts = " " * (spielfeldbreite - pos - leistenbreite)
 leiste = "=" * leistenbreite
 sys.stdout.write ('\r[' + leerlinks + leiste + leerrechts + ']')
 sys.stdout.flush()

 leerlinks  = " " * pos

 key = ord(msvcrt.getch())
 
 if key == 27:
  break

 elif key == 224:
  richtung = ord(msvcrt.getch())

  if richtung == 75:

   if pos > 0:
    pos = pos -1

   elif richtung == 77:

    if pos < (spielfeldbreite - leistenbreite):
     pos = pos +1

 if msvcrt.kbhit():
  key = ord(msvcrt.getch())

  if ord(key) == 32:
   print "Spacebar = Pressed"
   score = +1
   print score
   sys.exit(0)

