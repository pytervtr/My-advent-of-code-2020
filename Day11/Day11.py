import time 

def main():
	file = open("inputDay11","r")
	
	seatsArray=[]

	for line in file:
		seatsArray.append(line.rstrip("\n"))

	applyRules(seatsArray,4,0)

	print("------------------------------------")

	applyRules(seatsArray,5,1)




def applyRules(seatsArray,distance,mode):
	cambios = 0
	seatsArrayNew = seatsArray.copy()

	#imprime(seatsArray)
	while True:
		for seatsLine in range(len(seatsArray)):
			for seats in range(len(seatsArray[seatsLine])):


				if seatsArray[seatsLine][seats] == '#' and checkCosos(seatsArray, seatsLine,seats,mode) >= distance:

					cambios +=1
					seatsArrayNew[seatsLine]=seatsArrayNew[seatsLine][0:seats]+'L'+seatsArrayNew[seatsLine][seats+1:]

				elif seatsArray[seatsLine][seats] == 'L' and checkCosos(seatsArray,seatsLine,seats,mode) == 0:

					seatsArrayNew[seatsLine]=seatsArrayNew[seatsLine][0:seats]+'#'+seatsArrayNew[seatsLine][seats+1:]
					cambios +=1

		seatsArray = seatsArrayNew.copy()
		#imprime(seatsArray)

		if cambios == 0:
			break

		cambios = 0

	countVacancies(seatsArray)


def checkCosos(seatsArray,seatsLine,seats,mode):
	counter = 0

	if mode == 0:

		counter = checkUp(seatsArray,seatsLine,seats,0) + counter
		counter = checkDown(seatsArray,seatsLine,seats,0) + counter
		counter = checkRight(seatsArray,seatsLine,seats,0) + counter
		counter = checkLeft(seatsArray,seatsLine,seats,0) + counter
		counter = checkdRightUp(seatsArray,seatsLine,seats,0) + counter
		counter = checkdLeftUp(seatsArray,seatsLine,seats,0) + counter
		counter = checkdRightDown(seatsArray,seatsLine,seats,0) + counter
		counter = checkdLeftDown(seatsArray,seatsLine,seats,0) + counter

	elif mode != 0:

		counter = checkUp(seatsArray,seatsLine,seats,1) + counter
		counter = checkDown(seatsArray,seatsLine,seats,1) + counter
		counter = checkRight(seatsArray,seatsLine,seats,1) + counter
		counter = checkLeft(seatsArray,seatsLine,seats,1) + counter
		counter = checkdRightUp(seatsArray,seatsLine,seats,1) + counter
		counter = checkdLeftUp(seatsArray,seatsLine,seats,1) + counter
		counter = checkdRightDown(seatsArray,seatsLine,seats,1) + counter
		counter = checkdLeftDown(seatsArray,seatsLine,seats,1) + counter

	return counter




def checkUp(seatsArray,seatsLine,seats,mode):
	if seatsLine!=0 and seatsArray[seatsLine-1][seats] == '#' :	
		return 1

	elif mode == 1 and seatsLine!=0 and seatsArray[seatsLine-1][seats] == '.' :
		return checkUp(seatsArray,seatsLine-1,seats,mode)

	return 0

def checkDown(seatsArray,seatsLine,seats,mode):
	if seatsLine!=len(seatsArray)-1 and seatsArray[seatsLine+1][seats] == '#':
		return 1

	elif mode == 1 and seatsLine!=len(seatsArray)-1 and seatsArray[seatsLine+1][seats] == '.':
		return checkDown(seatsArray,seatsLine+1,seats,mode)

	return 0	

def checkRight(seatsArray,seatsLine,seats,mode):
	if seats != len(seatsArray[seatsLine])-1 and seatsArray[seatsLine][seats+1] == '#':
		return 1

	elif mode == 1 and seats != len(seatsArray[seatsLine])-1 and seatsArray[seatsLine][seats+1] == '.':
		return checkRight(seatsArray,seatsLine,seats+1,mode)

	return 0	

def checkLeft(seatsArray,seatsLine,seats,mode):
	if seats !=0 and seatsArray[seatsLine][seats-1] == '#':
		return 1

	elif mode == 1 and seats !=0 and seatsArray[seatsLine][seats-1] == '.':
		return checkLeft(seatsArray,seatsLine,seats-1,mode)

	return 0	

def checkdRightUp(seatsArray,seatsLine,seats,mode):
	if seatsLine!=0 and seats != len(seatsArray[seatsLine])-1 and seatsArray[seatsLine-1][seats+1] == '#':	
		return 1

	elif mode == 1 and seatsLine!=0 and seats != len(seatsArray[seatsLine])-1 and seatsArray[seatsLine-1][seats+1] == '.':	
		return checkdRightUp(seatsArray,seatsLine-1,seats+1,mode)

	return 0	

def checkdLeftUp(seatsArray,seatsLine,seats,mode):
	if seatsLine!=0 and seats!=0 and seatsArray[seatsLine-1][seats-1] == '#':
		return 1

	elif mode == 1 and seatsLine!=0 and seats!=0 and seatsArray[seatsLine-1][seats-1] == '.':
		return checkdLeftUp(seatsArray,seatsLine-1,seats-1,mode)

	return 0	

def checkdRightDown(seatsArray,seatsLine,seats,mode):
	if seatsLine!= len(seatsArray)-1 and seats!=len(seatsArray[seatsLine])-1 and seatsArray[seatsLine+1][seats+1] == '#':	
		return 1

	elif mode == 1 and seatsLine!= len(seatsArray)-1 and seats!=len(seatsArray[seatsLine])-1 and seatsArray[seatsLine+1][seats+1] == '.':	
		return checkdRightDown(seatsArray,seatsLine+1,seats+1,mode)

	return 0

def checkdLeftDown(seatsArray,seatsLine,seats,mode):
	if seatsLine!=len(seatsArray)-1 and seats!=0 and seatsArray[seatsLine+1][seats-1] == '#':
		return 1

	elif mode == 1 and seatsLine!=len(seatsArray)-1 and seats!=0 and seatsArray[seatsLine+1][seats-1] == '.':
		return checkdLeftDown(seatsArray,seatsLine+1,seats-1,mode)

	return 0



def countVacancies(seatsArray):
	counter = 0
	for seatsLine in seatsArray:
		counter = seatsLine.count("#")+counter
	print(counter)


main()

'''
def imprime(seatsArray):
	for seatsl in seatsArray:
		print(seatsl)
	print()
	print()

'''