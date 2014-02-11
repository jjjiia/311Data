import csv
import json
import collections

complaintTypes = ['noise']
complaintsInType = []
with open('../data/original/Case_Data_from_San_Francisco_311.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    coordinates = []
    print "opened"
    for row in spamreader:
        for complaint in complaintTypes:
            if complaint in row:
                print row
                complaintsInType.append(row)

print len(complaintsInType)

jsondump = json.dumps(complaintsInType)
file = open('../data/noise_all.json', 'w')
file.write(jsondump)