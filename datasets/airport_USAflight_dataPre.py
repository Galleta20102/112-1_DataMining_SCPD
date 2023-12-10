import csv

'''
Ｉ　Ａ　Ｂ　Ｇ </br>
８　０　１　６</br>
'Fly_date',　'Origin_airport',　'Destination_airport',　　'Flights'
'''

countData = {}
airports = []
fileFolder = "airport_USAflight/"
outfileName = "airport_USAflight"
dataset = open(fileFolder + "Airports2.csv", "r")

rows = csv.reader(dataset)

i=0
row = (next(rows))
for row in rows:
    
    row[8] = row[8].replace('/', '')
    fightRecord = row[8]+"_"+row[0]+"_"+row[1]
    
    if countData.get(fightRecord) ==  None:
        countData[fightRecord] = int(row[6])
    else: countData[fightRecord] += int(row[6])
        
    if row[0] not in airports:
        airports.append(row[0])
    if row[1] not in airports:
        airports.append(row[1])
    
countData = dict(sorted(countData.items()))
airports.sort()


'''
For txt output
'''
datasetSCPDFile = open(fileFolder + outfileName + '.txt', 'w')

for key in countData.keys():
    inData = key.split('_')
    datasetSCPDFile.write(inData[0] + "," + str(airports.index(inData[1])) + "," 
                              + str(airports.index(inData[2])) + "," + str(countData[key]) + '\n')
datasetSCPDFile.close()


'''
For csv output
'''
with open(fileFolder + outfileName + '.csv', 'w', newline='') as datasetSCPDFile:
    
    writerCsv = csv.writer(datasetSCPDFile)

    for key in countData.keys():
        inData = key.split('_')
        writerCsv.writerow([inData[0], airports.index(inData[1]), airports.index(inData[2]), countData[key]])

'''
For each Aairports Index
'''
AirportsIndexFile = open('AirportsIndex.txt', 'w')

for index in range(len(airports)):
    AirportsIndexFile.write(airports[index] + "," + str(index) + "\n")
    
AirportsIndexFile.close()