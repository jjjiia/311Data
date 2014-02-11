import csv
import json
import collections

#see nyc311_headers.csv for column headers

cleanedColumns = []
cleanedColumnsF = {}
#open file
with open('../data/nyc/noise_allconstruction.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    coordinates = []
    print "opened"
    
    for row in spamreader:
        #identify columns
        agency = row[4]
        descriptor = row[6]
        locationType = row[7]
        zipcode = row[9]
        borough = row[23]
        lat = row[49]
        lng = row[50]
        #make array of needed columns
        newrow = ['machine',agency,descriptor,locationType,zipcode,borough,lat,lng]
        newrowStr = str(newrow)
        #print newrow
        
        #make array of arrays
        cleanedColumns.append(newrowStr)
        #print cleanedColumns

for row in cleanedColumns:
    cleanedColumnsF[row]=cleanedColumnsF.get(row,0)+1

print cleanedColumnsF