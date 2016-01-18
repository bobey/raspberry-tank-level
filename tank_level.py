"""Water tank level

Usage:
  tank_level.py [-vsh] [--database-url=DB_URL]

Retrieve water tank current level and optionnaly store it in database.

Options:
  -h --help              show this help message and quit
  -v                     verbose mode
  -s                     store in database
  --database-url=DB_URL  the database url to connect to (mysql://user:passwd@ip:port/my_db)
"""

from datetime import datetime
from docopt import docopt
from RPi import GPIO
from peewee import *
from playhouse.db_url import connect

arguments = docopt(__doc__)
verbose = arguments['-v']
storeToDB = arguments['-s']
databaseUrl = arguments['--database-url'] or 'sqlite:///default.db'

database = connect(databaseUrl)

inputNumbers = [4, 7, 8, 9, 10, 11, 14, 15, 17, 18, 22]

class BaseModel(Model):
    class Meta:
        database = database

class Data(BaseModel):
    type = CharField()
    value = IntegerField()
    created_at = DateTimeField()

def setup_gpio():

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    for inputNumber in inputNumbers:
        GPIO.setup(inputNumber, GPIO.IN)

def get_level_from_index(index):
    if index == 10:
        return 3

    return 100 - index * 10

def display_tank_level():
    currentLevel = get_current_level()

    print currentLevel

    for (index, inputNumber) in enumerate(inputNumbers):
       indexLevel = get_level_from_index(index)
       percent = format(indexLevel, ' 4')
 
       if currentLevel < indexLevel:
           print "  ", percent, "%   |          |     GPIO ", inputNumber
       else:
           print "  ", percent, "%   |##########|     GPIO ", inputNumber

def get_current_level():
    for (index, inputNumber) in enumerate(inputNumbers):
        if GPIO.input(inputNumber):
            return get_level_from_index(index)

    return 0

def store_to_database():
    data = Data.create(type='filling', value=get_current_level(), created_at=datetime.now())

if __name__ == '__main__':

    setup_gpio()

    if storeToDB:
        store_to_database()

    if verbose:
        display_tank_level()
