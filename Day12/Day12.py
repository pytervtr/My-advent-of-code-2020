def main():

	instructions =[]

	file = open("inputDay12","r")

	for line in file:
		instructions.append(line.strip())


	sailingTest(instructions, 'E')
	sailingFinal(instructions, 'N', 'E', 1, 10)


def signDirection(newDirection):
	if newDirection == 'N' or newDirection == 'E':
		return 1

	elif newDirection == 'S' or newDirection == 'W':
		return -1

#height 
	#si positivo norte
	#si negativo sur
#distance
	#si positivo derecha
	#si negativo izquierda

#metodo que traza la direccion y el recorrido de un barco segun las instrucciones dadas
#para ello se tiene un contaador de direccion actual cuya funcion es determinar hacia que 
#posicion cardinal se direge y dos variables que almacenan las distancias cardinales
#tanto del eje X como del Y .

#cuando reciben una instruccion de avance lo hacen en la posicion a la que se dirige el barco
#cuando se desplaza hacia uno de los ejes cardinales lo suma a las variables de los ejes que correspondan
#y cuando tienen que girar el barco cambia la direccion a la que se dirige

def sailingTest(instructionList, currentDirection):

	directions = {'N':0,'E':90,'S':180,'W':270}
	degrees = {0:'N',90:'E',180:'S',270:'W'}



	currentSignDirection = signDirection(currentDirection)

	height = 0
	distance = 0


	for instruction in instructionList:
		
		action = instruction[0]
		value  = int(instruction[1:])

		if action == 'N':
			height = height + value

		elif action == 'S':
			height = height - value

		elif action == 'E':
			distance = distance + value

		elif action == 'W':
			distance = distance - value

		elif action == 'L' and directions[currentDirection]>= value:
			currentDirection = degrees[directions[currentDirection] - value]
			currentSignDirection = signDirection(currentDirection)

		elif action == 'L' and directions[currentDirection] < value:
			currentDirection = degrees[360 + directions[currentDirection] - value]
			currentSignDirection = signDirection(currentDirection)

		elif action == 'R':
			currentDirection = degrees[(directions[currentDirection] + value )%360]
			currentSignDirection = signDirection(currentDirection)


		elif action == 'F' and (currentDirection == 'N' or currentDirection == 'S'):
			height = height + (currentSignDirection * value )

		elif action == 'F' and (currentDirection == 'E' or currentDirection == 'W'):
			distance = distance + (currentSignDirection * value )
	

	print(abs(height)+abs(distance))

def checkHeight(currentHeight):
	if currentHeight >= 0:
		return 'N'
	elif currentHeight < 0:
		return 'S'

def checkDistance(currentDistance):
	if currentDistance >= 0:
		return 'E'
	elif currentDistance < 0:
		return 'W'

#height 
	#si positivo norte
	#si negativo sur
#distance
	#si positivo derecha
	#si negativo izquierda

#

#metodo que traza la direccion y el recorrido de un barco segun las instrucciones dadas
#para ello se tiene un contaador de direccion actual cuya funcion es determinar hacia que 
#posicion cardinal se direge y dos variables que almacenan las distancias cardinales
#tanto del eje X como del Y .

#cuando reciben una instruccion de avance lo hacen en la posicion a la que se dirige el barco
#estas modifcaciones se realizan teniendo encuenta ambos ejes el X y el Y
#cuando se desplaza hacia uno de los ejes cardinales incrementa o decrementa las variables de los ejes que correspondan
#y cuando tienen que girar el barco cambia la direccion a la que se dirige en ambos ejes

def sailingFinal(instructionList, initHeight, initDistance, incHeight, incDistance):

	directions = {'N':0,'E':90,'S':180,'W':270}
	degrees = {0:'N',90:'E',180:'S',270:'W'}

	height = 0
	distance = 0

	for instruction in instructionList:

		action = instruction[0]
		value = int(instruction[1:])

		if action == 'N':
			incHeight = incHeight + value
			initHeight = checkHeight(incHeight)

		elif action == 'S':
			incHeight = incHeight - value
			initHeight = checkHeight(incHeight)

		elif action == 'E':
			incDistance = incDistance + value
			initDistance = checkDistance(incDistance)

		elif action == 'W':
			incDistance = incDistance - value
			initDistance = checkDistance(incDistance)

		elif action == 'F' :
			height = height + incHeight*value
			distance = distance + incDistance*value

		elif action == 'R' and (value == 0 or value == 180):# si funciona I

			tempDir = degrees[(directions[initDistance] + value )%360]
			tempHei = 	 degrees[(directions[initHeight]+ value)%360]

			tempIncH = signDirection(tempHei) * abs(incHeight)
			tempIncD= signDirection(tempDir) * abs(incDistance)

			incHeight = tempIncH
			incDistance = tempIncD

			initHeight = tempHei
			initDistance = tempDir

		elif action == 'R' and (value == 90 or value == 270): # si funciona I
			
			tempDir = degrees[(directions[initDistance] + value )%360]
			tempHei = 	 degrees[(directions[initHeight]+ value)%360]

			tempIncD = signDirection(tempHei) * abs(incHeight)
			tempIncH = signDirection(tempDir) * abs(incDistance)

			incDistance = tempIncD
			incHeight = tempIncH 

			initHeight = tempDir
			initDistance = tempHei

		elif action == 'L' and (value == 0 or value == 180): # si funciona	I

			tempDir = degrees[(360 + directions[initDistance] - value) % 360]
			tempHei = degrees[(360 + directions[initHeight] - value) % 360]

			tempIncH = signDirection(tempHei) * abs(incHeight)
			tempIncD= signDirection(tempDir) * abs(incDistance)

			incHeight = tempIncH
			incDistance = tempIncD

			initHeight = tempHei
			initDistance = tempDir

		elif action == 'L' and (value == 90 or value== 270):#si funciona

			tempDir = degrees[(360 + directions[initDistance] - value) % 360]
			tempHei = degrees[(360 + directions[initHeight] - value) % 360]

			tempIncD= signDirection(tempHei) * abs(incHeight)
			tempIncH = signDirection(tempDir) * abs(incDistance)

			incHeight = tempIncH
			incDistance = tempIncD			

			initHeight = tempDir
			initDistance = tempHei

	print(abs(height)+abs(distance))


main()