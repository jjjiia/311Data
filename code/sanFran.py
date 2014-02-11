import csv
complaintTypes = []
complaintTypesFreq = {}

##make an array of the column you want
with open('../data/original/Case_Data_from_San_Francisco_311.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        coordinates = []
        print "opened"
        for row in spamreader:
            
            complaintType = row[8]
            ##print complaintType
            complaintTypes.append(complaintType)
        print len(complaintTypes)

## make a dictionary of frequency of occurence in that column
for i in complaintTypes:
    complaintTypesFreq[i] = complaintTypesFreq.get(i, 0)+1

print complaintTypesFreq
