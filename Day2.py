def main():
	file = open("inputDay2","r")
	#validaRangos(file)
	validaPosiciones(file)
	file.close()

def validaRangos(file):
	max = 0
	min = 0
	char = ""

	contrasenasValidas = 0

	for line in file:
		min = int(line[:line.index("-")])
		max = int(line[line.index("-")+1:line.index(" ")])
		char = line[line.index(" ")+1:line.index(":")]
		
		if (line.count(char)-1) >= min and (line.count(char)-1) <= max:
			contrasenasValidas += 1

	print(contrasenasValidas)

def validaPosiciones(file):
	posicion1 = 0
	posicion2 = 0
	char = ""
	contrasena = ""

	contrasenasValidas = 0

	for line in file:
		posicion1 = int(line[:line.index("-")])-1
		posicion2 = int(line[line.index("-")+1:line.index(" ")])-1
		char = line[line.index(" ")+1:line.index(":")]
		contrasena = line[line.index(": ")+2:]
	
		if(contrasena[posicion1] is char and contrasena[posicion2] is not char):
			contrasenasValidas +=1
		elif(contrasena[posicion1] is not char and contrasena[posicion2] is char):
			contrasenasValidas +=1

	print(contrasenasValidas)


main()