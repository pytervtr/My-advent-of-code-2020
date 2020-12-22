def main():

	arrayMochilas = []
	diccMochilasParseadas = {}

	file = open("inputDay07","r")

	for line in file:
		arrayMochilas.append(line.rstrip(".\n"))


	diccMochilasParseadas = parseaEntrada(arrayMochilas)
	cuentaColoresMochila( diccMochilasParseadas)

	print(cuentaTotalMochilas(diccMochilasParseadas, "shiny gold bag",1))

def parseaEntrada(arrayMochilas):

	arrayMochilasParseadas = []
	diccMochilasParseadas = {}

	indice = ""

	for lineaMochila in arrayMochilas :
		if(lineaMochila.count(",")==0):

			indice = lineaMochila[:lineaMochila.index(" bag")+4]

			lineaMochila = lineaMochila[lineaMochila.index(" contain")+9:]

			arrayMochilasParseadas.append(lineaMochila[:lineaMochila.index(" ")])									#guarda numero

			arrayMochilasParseadas.append(lineaMochila[lineaMochila.index(" ")+1:lineaMochila.index(" bag")+4])		#guarda mochila

			diccMochilasParseadas[indice] = arrayMochilasParseadas.copy()

			arrayMochilasParseadas = []


			

		else:


			indice = lineaMochila[:lineaMochila.index(" bag")+4]

			lineaMochila = lineaMochila[lineaMochila.index(" contain")+9:]

			for x in range (lineaMochila.count(",")):

				arrayMochilasParseadas.append(lineaMochila[:lineaMochila.index(" ")])									#Agrega numero 
				arrayMochilasParseadas.append(lineaMochila[lineaMochila.index(" ")+1:lineaMochila.index(" bag")+4])		#Agrega tipo mochila

				lineaMochila = lineaMochila[lineaMochila.index(",")+2:]

			arrayMochilasParseadas.append(lineaMochila[:lineaMochila.index(" ")])										#Agrega numero 
			arrayMochilasParseadas.append(lineaMochila[lineaMochila.index(" ")+1:lineaMochila.index(" bag")+4])			#Agrega tipo mochila


			diccMochilasParseadas[indice] = arrayMochilasParseadas.copy()
			arrayMochilasParseadas = []

	return diccMochilasParseadas

def cuentaColoresMochila(diccMochilasParseadas): 

	mochilas_visitadas = set()
	mochilas_validas = {'shiny gold bag':0}

	for claveMochila in diccMochilasParseadas.keys():
		for claveMochilaIteracion in diccMochilasParseadas.keys():

			buscaColoresMochilas(mochilas_visitadas, mochilas_validas, claveMochilaIteracion, diccMochilasParseadas)

		mochilas_visitadas = set()

	print(len(mochilas_validas)-1)

def buscaColoresMochilas(mochilas_visitadas, mochilas_validas, claveMochilaIteracion,diccMochilasParseadas):

	if claveMochilaIteracion not in mochilas_visitadas:
		mochilas_visitadas.add(claveMochilaIteracion)

		for posicionMochila in range(len(diccMochilasParseadas[claveMochilaIteracion])):

			if diccMochilasParseadas[claveMochilaIteracion][posicionMochila] == 'no':

				return 

			elif( posicionMochila %2 != 0 and diccMochilasParseadas[claveMochilaIteracion][posicionMochila] in mochilas_validas):

				mochilas_validas[claveMochilaIteracion] = 0
				return 
				#buscaColoresMochilas(mochilas_visitadas, mochilas_validas, diccMochilasParseadas[claveMochilaIteracion][posicionMochila], diccMochilasParseadas) 


def cuentaTotalMochilas(diccMochilasParseadas, claveMochila, almacenador):

	total = 0
	for values in range(len(diccMochilasParseadas[claveMochila])):
		if diccMochilasParseadas[claveMochila][values] == "no":
			return 0
		elif values % 2 !=0:
			
			#print (total,claveMochila,diccMochilasParseadas[claveMochila])
			total = total + int(diccMochilasParseadas[claveMochila][values-1]) +  int(diccMochilasParseadas[claveMochila][values-1])*int(cuentaTotalMochilas(diccMochilasParseadas,diccMochilasParseadas[claveMochila][values], almacenador*int(diccMochilasParseadas[claveMochila][values-1])))
			#print (total,claveMochila,diccMochilasParseadas[claveMochila])

	#print (total,claveMochila,diccMochilasParseadas[claveMochila])
	return total

main()