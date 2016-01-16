"""Water tank level

Usage:
  tank_level.py [-vsh]

Retrieve water tank current level and optionnaly store it in database.

Options:
  -h --help  show this help message and quit
  -v         verbose mode
  -s         store in database
"""

from docopt import docopt
from RPi import GPIO

if __name__ == '__main__':
    arguments = docopt(__doc__)
    verbose = arguments['-v']

    outputs = [4, 7, 8, 9, 10, 11, 14, 15, 17, 18, 22];
 
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
 
    for i in range(0, 11):
        GPIO.setup(outputs[i], GPIO.IN)
 
    for i in range(0, 11):
 
       if (i == 0):
          P = "100"
       elif (i == 1):
          P = " 90"
       elif (i == 2):
          P = " 80"
       elif (i == 3):
          P = " 70"
       elif (i == 4):
          P = " 60"
       elif (i == 5):
          P = " 50"
       elif (i == 6):
          P = " 40"
       elif (i == 7):
          P = " 30"
       elif (i == 8):
          P = " 20"
       elif (i == 9):
          P = " 10"
       elif (i == 10):
          P = "  3"
 
 
       if GPIO.input(outputs[i]) == False:
           if verbose :
               print "  ",P,"%   |          |     GPIO ",outputs[i]
           else:
               print "  ",P,"%   |          |"
       else:
           if verbose :
              print "  ",P,"%   |##########|     GPIO ",outputs[i]
           else:
              print "  ",P,"%   |##########|"
