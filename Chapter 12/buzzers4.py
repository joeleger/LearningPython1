import pprint as pp
from datetime import datetime

"""
    Comprehensions for dictionaries and lists
"""


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


"""Create the main list and dictionary """
with(open('buzzers.csv')) as data:
    ignore = data.readline()  # we do not need the header
    flights = {}
    for line in data:
        k, v = line.strip().split(',')  # strips the line, then splits it, to produce the data in the format required
        flights[k] = v  # assign  destination to flight time
    pp.pprint(flights)
    print()
    flights2 = {}
    for k, v in flights.items():
        flights2[convert2ampm(k)] = v.title()
    pp.pprint(flights2)
    print()
"""Create comprehensions for the above
"""
# first create a list of times comprehension
fts2 = [convert2ampm(ft) for ft in flights.keys()]
# now create a list of destinations comprehension
more_dests = [dest.title() for dest in flights.values()]

# create a dictionary comprehension
more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}
pp.pprint(more_flights)
print()
# FILTERS
# Just Freeport
just_freeport = {}
for k, v in flights.items():
    if v == 'FREEPORT':
        just_freeport[convert2ampm(k)] = v.title()
pp.pprint(just_freeport)
print()

# Just Freeport as a Comprehension
just_freeport2 = {convert2ampm(k): v.title() for k, v in flights.items() if v == 'FREEPORT'}
pp.pprint(just_freeport2)
print()

# EXERCISES
data = [1, 2, 3, 4, 5, 6, 7, 8]
evens = []
for num in data:
    if not num % 2:
        evens.append(num)
pp.pprint(evens)
print()
# Convert to list comprehension
evens_new = [num for num in data if not num % 2]
pp.pprint(evens_new)
print('List comprehension')

data = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = []
for num in data:
    if isinstance(num, str):
        words.append(num)
pp.pprint(words)
print()
# Convert to list comprehension
words_new = [num for num in data if isinstance(num, str)]
pp.pprint(words_new)
print('List comprehension2')

data = list('So long and thanks for all the fish'.split())
title = []
for word in data:
    title.append(word.title())
pp.pprint(title)
print()
# Convert to title case
title_new = [word.title() for word in data]
pp.pprint(title_new)
print('List comprehension3')

"""Now we need to swap the value keys so that we can uniqueify the destination"""

"""Here is the dictionary of flight times and destinations"""
fts = {convert2ampm(k): v.title() for k, v in flights.items()}
# Here is how to make the destinations unique
dests = set(fts.values())
# now the loop
when = {}
for dest in set(fts.values()):
    when[dest] = [k for k, v in fts.items() if v == dest]
pp.pprint(when)
print()
# now convert this to a comprehension
when2 = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}
pp.pprint(when2)
print('Dictionary comprehension')

"""Set Comprehensions"""
vowels = {'a', 'e', 'i', 'o', 'u'}
message = "Don't forget to pack your towel."
"""typical for loop"""
found = set()
for v in vowels:
    if v in message:
        found.add(v)
pp.pprint(found)
print()

#Convert to setcomp
found2 = {v for v in vowels if v in message}
pp.pprint(found)
print('SetComp')



