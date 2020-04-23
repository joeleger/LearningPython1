import csv

"""
    1 Convert the flight times from 24-hour format to AM/PM format
"""

with(open('buzzers.csv')) as data:
    ignore = data.readline() # we do not need the header
    flights = {}
    for line in data:
        k,v = line.strip().split(',') # strips the line, then splits it, to produce the data in the format required
        flights[k] = v # assign  destination to flight time
        print(line)

