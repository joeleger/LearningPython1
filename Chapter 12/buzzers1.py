import csv

"""transform the raw data in your CSV file into a collection of Python
dictionaries."""
with(open('buzzers.csv')) as data:
    for line in csv.DictReader(data):
        print(line)

