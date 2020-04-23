import pprint
from datetime import datetime

"""
    1 Convert the flight times from 24-hour format to AM/PM format
    2 Convert the destinations from UPPERCASE to Titlecase
"""
""""
Given a time in 24-hour format (as a
string), this method chain converts it
into a string in AM/PM format.
"""


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with(open('buzzers.csv')) as data:
    ignore = data.readline()  # we do not need the header
    flights = {}
    for line in data:
        k, v = line.strip().split(',')  # strips the line, then splits it, to produce the data in the format required
        flights[k] = v  # assign  destination to flight time
    pprint.pprint(flights)
    print()
    flights2 = {}
    for k, v in flights.items():
        flights2[convert2ampm(k)] = v.title()
    pprint.pprint(flights2)
