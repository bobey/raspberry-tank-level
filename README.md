# RaspberryPI (water) Tank Level

Basic command line script in Python to retrieve tank level with Raspberry and optionnaly store it in database.

## Usage

```
  tank_level.py [-vsh] [--database-url=DB_URL]
  
  Options:
  -h --help              show this help message and quit
  -v                     verbose mode
  -s                     store in database
  --database-url=DB_URL  the database url to connect to (mysql://user:passwd@ip:port/my_db)
```

## Requirements

- PyMysql or equivalent
- RPi.GPIO

## Credits

Inspired by [Frederic JELMONI project](http://www.fred-j.org/?p=364)
