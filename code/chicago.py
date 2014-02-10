import csv
complaintTypes = []
complaintTypesFreq = {}

##make an array of the column you want
with open('../data/original/CDPH_Environmental_Complaints.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        coordinates = []
        print "opened"
        for row in spamreader:
            print row
            complaintType = row[1]
            complaintTypes.append(complaintType)
        print len(complaintTypes)

## make a dictionary of frequency of occurence in that column
for i in complaintTypes:
    complaintTypesFreq[i] = complaintTypesFreq.get(i, 0)+1

print complaintTypesFreq
