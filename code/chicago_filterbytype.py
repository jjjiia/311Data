import csv
import json
import collections

complaintTypes = ['Noise Complaint', 'NOISE COMPLAINT']
complaintsInType = []
with open('../data/original/CDPH_Environmental_Complaints.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    coordinates = []
    print "opened"
    for row in spamreader:
        for complaint in complaintTypes:
            if complaint in row:
                #print row
                complaintsInType.append(row)

print len(complaintsInType)

jsondump = json.dumps(complaintsInType)
file = open('../data/noise_all.json', 'w')
file.write(jsondump)