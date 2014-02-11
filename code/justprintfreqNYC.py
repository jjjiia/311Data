import csv
import json
import collections
frequency = []
with open('../data/noise_allconstruction_coordinatesfreq.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    coordinates = []
    print "opened"
    for row in spamreader:
        frequency.append(row[-1])
        
print frequency
        