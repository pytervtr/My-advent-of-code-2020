def main():

	result = -1
	listDisplay = []
	file = open("inputDay09", "r")
	
	for line in file:
		listDisplay.append(line.rstrip("\n"))



	result = checkXMASCodesRange(listDisplay)
	
	if result != -1:
		checkWeaknessSum(result, listDisplay)

def checkXMASCodesRange(listDisplay):
	for currentPosition in range (25,len(listDisplay)):
		if False == checkAddRange(listDisplay[currentPosition],listDisplay[currentPosition-25:currentPosition]):
			print(listDisplay[currentPosition])
			return listDisplay[currentPosition]
		#print(listDisplay[currentCode-25:currentCode], len(listDisplay[currentCode-25:currentCode]), listDisplay[currentCode])

	return -1

def checkAddRange(searchNumber, listDisplayNumbers):

	for currentCodeNumber in listDisplayNumbers:
		if str(abs(int(currentCodeNumber)-int(searchNumber))) in listDisplayNumbers:
			return True

	return False

def checkWeaknessSum(goal, listDisplay):
	listDisplayIntegers = list(map(int, listDisplay))
	result = -1
	for currentPosition in range(len(listDisplayIntegers)):
		result = checkSumWeaknessRange(int(goal), currentPosition, currentPosition,listDisplayIntegers)
		if result != -1:
			getWeaknessEncriptation(listDisplayIntegers[currentPosition:result])
			break


def checkSumWeaknessRange(goal, initPosition, currentPosition, listDisplayIntegers):


	if currentPosition <= len(listDisplayIntegers) and sum(listDisplayIntegers[initPosition:currentPosition]) == goal :
		return currentPosition

	elif currentPosition <= len(listDisplayIntegers) and sum(listDisplayIntegers[initPosition:currentPosition]) < goal :
		return checkSumWeaknessRange(goal, initPosition, currentPosition+1, listDisplayIntegers)

	elif currentPosition > len(listDisplayIntegers)  or sum(listDisplayIntegers[initPosition:currentPosition]) > goal :
		return -1

def getWeaknessEncriptation(listDisplayIntegers):
	listDisplayIntegers.sort()
	print(listDisplayIntegers[0]+listDisplayIntegers[len(listDisplayIntegers)-1])
main()