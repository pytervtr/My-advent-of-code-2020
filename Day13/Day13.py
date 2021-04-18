import math

def main():

	inputData = parseInput()

	findSoonerBus(inputData)

	continuousArrival(inputData)




#KEY 	=> INDEX_BUS
#VALUE 	=> ID_BUS

def parseInput():
	file = open("input","r")

	parseData = {}

	index = -1


	for line in file:
		for position in range(line.count(",")):
			bus = line[:line.index(",")]
			if bus.isdigit():
				parseData[index]=int(bus.strip())
			index+=1

			line = line[line.index(",")+1:]

		parseData[index]=int(line.strip())
		index+=1

	return parseData

def findSoonerBus(inputData):


	soonerBuses = {}

	initTime = inputData[-1]

	for rawBusIndex, rawBusId in inputData.items():
		if rawBusIndex != -1:
			parseBus = math.ceil(initTime/rawBusId)*rawBusId
			soonerBuses[parseBus] = inputData[rawBusIndex]


	result = (min(soonerBuses.keys())-initTime)*soonerBuses[min(soonerBuses.keys())] 

	print(result)



def continuousArrival(inputData):

	frontier = inputData[-1]
	inputData.pop(-1)

	time = 0
	stepSize = 1
	stepForward = 0

	for index in inputData:
		time = continuousArrivalRec(time,stepSize,index,inputData[index])
		stepSize = stepSize * inputData[index]
	print(time)



def continuousArrivalRec(time,stepSize,index,busId):
	
	if ((time+index)%busId) == 0:
		return time
	else:
		return continuousArrivalRec((time+stepSize),stepSize,index,busId)

main()