import copy
import re 


def main():
	parseArray = []

	file = open("inputDay4","r")
	
	for line in file:
		tempS = line.rstrip("\n")
		if(tempS != "") and len(parseArray)==0:
			parseArray.append(tempS+" ")
		elif(tempS != "") :
			tempS = str(parseArray[len(parseArray)-1])+tempS+" "
			parseArray[len(parseArray)-1] = tempS
		else:
			parseArray.append("")

	file.close()


	#validaPasaporteSalto(parseArray)
	validaPasaporteCompleto(parseArray)

def parseaDiccionario(parseArray):
	clave= ""
	valor = ""
	tempS = ""

	arrayDiccionarios = []
	dicc = {}
	for line in parseArray:

			
		for x in range (line.count(" ")):
			tempS = line[:line.index(" ")]#campo actual del pasaporte 

			clave = tempS[:tempS.index(":")]
			valor = tempS[tempS.index(":")+1:]

			dicc[clave]=str(valor)

			line = line[line.index(" ")+1:]

		arrayDiccionarios.append({})
		arrayDiccionarios[len(arrayDiccionarios)-1] = copy.deepcopy(dicc)
		dicc.clear()
	return arrayDiccionarios


def validaPasaporteSalto(parseArray):


	arrayDiccionarios = parseaDiccionario(parseArray)
	pasaportesValidos = 0


	for posicion in range(0, len(arrayDiccionarios)):
		if len(arrayDiccionarios[posicion]) == 8:
			pasaportesValidos +=1 
		elif len(arrayDiccionarios[posicion]) == 7 and 'cid' not in arrayDiccionarios[posicion]:
			pasaportesValidos +=1



	print("El total es", pasaportesValidos)


def validaPasaporteCompleto(parseArray):
	arrayDiccionarios = parseaDiccionario(parseArray)
	pasaportesValidos = 0
	camposValidos = 0
	substringPelo = "[a-f]|[0-9]"	
	substringID = "[0-9]"

	for posicion in range(0, len(arrayDiccionarios)):
		if len(arrayDiccionarios[posicion]) == 8 or len(arrayDiccionarios[posicion]) == 7:
			if 'byr' in arrayDiccionarios[posicion] and int(arrayDiccionarios[posicion]['byr']) >= 1920 and int(arrayDiccionarios[posicion]['byr']) <= 2002:
				camposValidos +=1

			if 'iyr' in arrayDiccionarios[posicion] and int(arrayDiccionarios[posicion]['iyr']) >= 2010 and int(arrayDiccionarios[posicion]['iyr']) <= 2020:
				camposValidos +=1

			if 'eyr' in arrayDiccionarios[posicion] and int(arrayDiccionarios[posicion]['eyr']) >= 2020 and int(arrayDiccionarios[posicion]['eyr']) <= 2030:
				camposValidos +=1

			if ('hgt' in arrayDiccionarios[posicion] and "cm" in arrayDiccionarios[posicion]['hgt'] 
				and int(arrayDiccionarios[posicion]['hgt'][:arrayDiccionarios[posicion]['hgt'].index("cm")]) >= 150 
				and int(arrayDiccionarios[posicion]['hgt'][:arrayDiccionarios[posicion]['hgt'].index("cm")]) <= 193):
					camposValidos +=1
		
			elif ('hgt' in arrayDiccionarios[posicion] and "in" in arrayDiccionarios[posicion]['hgt'] 
				and int(arrayDiccionarios[posicion]['hgt'][:arrayDiccionarios[posicion]['hgt'].index("in")]) >= 59 
				and int(arrayDiccionarios[posicion]['hgt'][:arrayDiccionarios[posicion]['hgt'].index("in")]) <= 76):
					camposValidos +=1
		
			if ('hcl' in arrayDiccionarios[posicion] and len(arrayDiccionarios[posicion]['hcl']) == 7 and arrayDiccionarios[posicion]['hcl'][0] == "#" 
				and len(re.findall(substringPelo,arrayDiccionarios[posicion]['hcl']))==6):
				camposValidos +=1			

			if 'ecl' in arrayDiccionarios[posicion] and arrayDiccionarios[posicion]['ecl'] in ["amb","blu","brn","gry","grn","hzl","oth"]:
				camposValidos +=1


			if 'pid' in arrayDiccionarios[posicion] and len(re.findall(substringID,arrayDiccionarios[posicion]['pid']))==9:
				camposValidos +=1
			
			if 'cid' in arrayDiccionarios:
				camposValidos +=1

			if(camposValidos ==8 or camposValidos ==7):
				pasaportesValidos +=1 
			camposValidos = 0
	
	print("El total es", pasaportesValidos)

main()