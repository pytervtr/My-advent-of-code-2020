def main():

	arrayAsientos = []
	file = open("inputDay5","r")

	for line in file:
		arrayAsientos.append(line.strip("\n"))

	file.close()
	buscaAsientoMax(arrayAsientos)
	buscaMiAsiento(arrayAsientos)

def buscaAsientoMax(arrayAsientos):
	asientoMaximo = 0
	asientoTemp = 0
	fila = ['F','B']
	columna = ['L','R']
	for asiento in arrayAsientos:
		if len(asiento) == 10:
			asientoTemp = buscaPosicionAsientoRec(asiento[:-3], 0, 128, fila)
			asientoTemp = asientoTemp *8 + buscaPosicionAsientoRec(asiento[-3:],0,8, columna)
			if asientoTemp > asientoMaximo:
				asientoMaximo = asientoTemp
		asientoTemp = 0
	print(asientoMaximo)


def buscaPosicionAsientoRec(asiento, min, max, position):
	if len(asiento)==0:
		return min
	if asiento[0] == position[0]:
		desplazamiento = (max - min)/2
		return buscaPosicionAsientoRec(asiento[1:], min, max - desplazamiento, position)
	elif asiento[0] == position[1]:
		desplazamiento = (max - min)/2
		return buscaPosicionAsientoRec(asiento[1:], desplazamiento + min, max, position)
	return 0			#en caso de errror

def buscaMiAsiento(arrayAsientos):
	asientos = [] 
	valorAsiento = 0
	fila = ['F','B']
	columna = ['L','R']

	valorInferior=0
	valorSuperior=0

	for asiento in arrayAsientos:
		if len(asiento) == 10:
			valorAsiento = buscaPosicionAsientoRec(asiento[:-3], 0, 128, fila)
			valorAsiento = valorAsiento *8 + buscaPosicionAsientoRec(asiento[-3:],0,8, columna)

			asientos.append(valorAsiento)

		valorAsiento = 0

	asientos.sort()
	for contador in range(len(asientos)):
		#print(asientos[contador])
		#print(contador)
		#print(asientos[contador]+asientos[len(asientos)-1-contador],asientos[contador]+asientos[len(asientos)-1])		
		#print(asientos[contador],asientos[len(asientos)-1-contador])
		if(asientos[contador]+asientos[len(asientos)-1-contador])!=(asientos[0]+asientos[len(asientos)-1]):

			valorInferior = asientos[contador]
			valorSuperior = asientos[len(asientos)-1-contador]
			
			if valorInferior-1 == asientos[contador-1] and valorInferior+1 != asientos[contador+1]:
				print(valorInferior+1)
				break
			elif valorInferior-1 != asientos[contador-1] and valorInferior+1 == asientos[contador+1]:
				print(valorInferior-1)
				break
			
			if valorSuperior-1 == asientos[len(asientos)-1-contador-1] and valorSuperior+1 != asientos[len(asientos)-1-contador+1]:
				print(valorSuperior+1)			
				break

			elif valorSuperior-1 != asientos[len(asientos)-1-contador-1] and valorSuperior+1 == asientos[len(asientos)-1-contador+1]:
				print(valorSuperior+1)
				break
			
main()