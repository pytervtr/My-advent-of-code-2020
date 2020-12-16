def main():

										#[3,1]	#primer ejercicio
	sloopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]	#segundo ejercicio
	tablero = []
	nArboles = 0

	file = open("inputDay3","r")

	for line in file:
		tablero.append(line.rstrip("\n"))	#guardado sin salto de linea

	file.close()
	
	nArboles = recorreCamino(tablero,3,1)	# primer ejercicio
	print("Primer challenge", nArboles)

	nArboles = 0							#segundo ejercicio

	for x in sloopes:
		tmp = recorreCamino(tablero, x[0], x[1])

		if(nArboles == 0):
			nArboles = tmp
		else:
			nArboles = nArboles * tmp

	print("Segundo challenge",nArboles)


def recorreCamino(tablero, aumentoX, aumentoY):

	posX_actual = 0
	posY_actual = 0

	

	nArboles = 0

	while posY_actual < len(tablero)-1:

		posX_actual +=aumentoX
		posX_actual = posX_actual % (len(tablero[0]))
		posY_actual +=aumentoY
			

		if ord(tablero[posY_actual][posX_actual]) == ord('#'):
			nArboles = nArboles + 1		

	return nArboles


main()

