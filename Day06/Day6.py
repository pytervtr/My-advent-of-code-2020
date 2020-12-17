import copy

def main():

	arrayEncuesta = []
	arrayEncuestaParseado = []
	file = open("inputDay6","r")

	for line in file:
		arrayEncuesta.append(line.rstrip("\n"))

	arrayEncuestaParseado = parseaEntrada(arrayEncuesta)
	calculaEncuesta(arrayEncuestaParseado)
	calculaEncuestasCorrectas(arrayEncuestaParseado)

def parseaEntrada(arrayEncuesta):
	diccT = {}
	diccF = {}
	contador = 0
	contadorEncuestas = 0
	arrayParseado = []
	for numeroEncuesta in range(len(arrayEncuesta)):
		if arrayEncuesta[numeroEncuesta] != "" :
			for caracter in (arrayEncuesta[numeroEncuesta]):
				if caracter in diccT:
					diccT[caracter] = diccT[caracter] + 1 
				else:
					diccT[caracter] = 1
			diccF.update(diccT)
			contadorEncuestas +=1
		else:
			arrayParseado.insert(len(arrayParseado)-1, [contadorEncuestas, copy.deepcopy(diccF)])
			diccF.clear()
			diccT.clear()
			contadorEncuestas = 0
		if numeroEncuesta == len(arrayEncuesta)-1:
			arrayParseado.insert(len(arrayParseado)-1, [contadorEncuestas, copy.deepcopy(diccF)])
			diccF.clear()
			diccT.clear()
			contadorEncuestas = 0
		contador+=1
	return arrayParseado

def calculaEncuesta(arrayEncuestaParseado):
	contador = 0
	for elementos in range(len(arrayEncuestaParseado)):
		contador = contador + len(arrayEncuestaParseado[elementos][1])

	print(contador)
	
def calculaEncuestasCorrectas(arrayEncuestaParseado):
	contador = 0
	for encuesta in (arrayEncuestaParseado):
		for preguntas in (encuesta[1].keys()):
			if encuesta[1][preguntas] == encuesta[0]:
				contador +=1 
	print(contador)

main()