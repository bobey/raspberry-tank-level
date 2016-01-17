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

You probably want to plan this script execution every few hours to collect workable data.
Add the following in some of your Raspberry PI crontab:

```
* */6 * * * /usr/bin/python2.7 /path/to/tank_level.py --database-url=mysql://user:passwd@ip:port/my_db -s >/dev/null 2>&1
```

After a few months of execution, you should be able to extract some nice graphs as the following:

![Raspberry tank level graph visualization](https://raw.githubusercontent.com/bobey/raspberry-tank-level/master/assets/tank_level_raspberry.png)

For those asking, I chose to visualize data with [Metabase](http://www.metabase.com/) simple BI tool.

## Requirements

- PyMysql or equivalent
- RPi.GPIO

## Credits

Inspired by [Frederic JELMONI project](http://www.fred-j.org/?p=364)
