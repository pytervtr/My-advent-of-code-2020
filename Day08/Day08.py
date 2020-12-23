import copy

def main():

	arrayInstructions = []
	diccInstrucctionsParsed = {}

	file = open("inputDay08","r")

	for line in file:
		arrayInstructions.append(line.rstrip("\n"))

	diccInstrucctionsParsed =  parseInput(arrayInstructions)
	countValue(diccInstrucctionsParsed)

	diccInstrucctionsParsed = fixCorruptedCode(diccInstrucctionsParsed)
	countValue(diccInstrucctionsParsed)

def parseInput(arrayInstructions):

	diccInstrucctionsParsed = {}
	arrayValues = []
	counter = 0

	for instrucction in arrayInstructions:
		arrayValues.append(instrucction[:instrucction.index(" ")])
		arrayValues.append(instrucction[instrucction.index(" ")+1:])
		diccInstrucctionsParsed[counter] = copy.deepcopy(arrayValues)

		arrayValues = []
		counter +=1

	return diccInstrucctionsParsed

def countValue(diccInstrucctionsParsed):

	currentInstruction = 0
	accValue = 0
	visitedInstrucctions = []

	accValue = execBootProgram(diccInstrucctionsParsed, currentInstruction, accValue, visitedInstrucctions)
	print(accValue)

def execBootProgram(diccInstrucctionsParsed, currentInstruction, accValue, visitedInstrucctions):

	if currentInstruction in visitedInstrucctions or int(currentInstruction)>= len(diccInstrucctionsParsed):
		return accValue
	else:
		visitedInstrucctions.append(currentInstruction)
		if diccInstrucctionsParsed[currentInstruction][0] == "jmp":
			return execBootProgram(diccInstrucctionsParsed, currentInstruction+(int(diccInstrucctionsParsed[currentInstruction][1])), accValue, visitedInstrucctions)

		elif diccInstrucctionsParsed[currentInstruction][0] == "acc":
			return execBootProgram(diccInstrucctionsParsed, currentInstruction+1, accValue+(int(diccInstrucctionsParsed[currentInstruction][1])), visitedInstrucctions)

		elif diccInstrucctionsParsed[currentInstruction][0] == "nop":
			return execBootProgram(diccInstrucctionsParsed, currentInstruction+1, accValue, visitedInstrucctions)			

def fixCorruptedCode(diccInstrucctionsParsed):

	result = 0
	visitedInstrucctions = []


	for key in diccInstrucctionsParsed:
		if diccInstrucctionsParsed[key][0] != "acc" and diccInstrucctionsParsed[key][0] =="jmp":

			diccInstrucctionsParsed[key]=copy.deepcopy(['nop', diccInstrucctionsParsed[key][1]])
			result = execBootProgramRepes(diccInstrucctionsParsed, 0, 0, visitedInstrucctions)

			if result == 0:
				break

			diccInstrucctionsParsed[key]=copy.deepcopy(['jmp', diccInstrucctionsParsed[key][1]])
			
		elif diccInstrucctionsParsed[key][0] != "acc" and diccInstrucctionsParsed[key][0] =="nop":

			diccInstrucctionsParsed[key]=copy.deepcopy(['jmp', diccInstrucctionsParsed[key][1]])	
			result = execBootProgramRepes(diccInstrucctionsParsed, 0, 0, visitedInstrucctions)

			if result == 0:
				break

			diccInstrucctionsParsed[key]=copy.deepcopy(['nop', diccInstrucctionsParsed[key][1]])	

		visitedInstrucctions = []

	return diccInstrucctionsParsed


def execBootProgramRepes(diccInstrucctionsParsed, currentInstruction, accValue, visitedInstrucctions):

	if currentInstruction in visitedInstrucctions:
		return 1

	elif currentInstruction not in visitedInstrucctions and int(currentInstruction)<len(diccInstrucctionsParsed)-1:
		visitedInstrucctions.append(currentInstruction)

		if diccInstrucctionsParsed[currentInstruction][0] == "jmp":
			return execBootProgramRepes(diccInstrucctionsParsed, currentInstruction+(int(diccInstrucctionsParsed[currentInstruction][1])), accValue, visitedInstrucctions)

		elif diccInstrucctionsParsed[currentInstruction][0] == "acc":
			return execBootProgramRepes(diccInstrucctionsParsed, currentInstruction+1, accValue+(int(diccInstrucctionsParsed[currentInstruction][1])), visitedInstrucctions)

		elif diccInstrucctionsParsed[currentInstruction][0] == "nop":
			return execBootProgramRepes(diccInstrucctionsParsed, currentInstruction+1, accValue, visitedInstrucctions)	

	elif currentInstruction not in visitedInstrucctions and int(currentInstruction)==len(diccInstrucctionsParsed)-1:	

		if	diccInstrucctionsParsed[currentInstruction][0] == "acc" or diccInstrucctionsParsed[currentInstruction][0] == "nop":
			return 0

		elif diccInstrucctionsParsed[currentInstruction][0] == "jmp" and int(diccInstrucctionsParsed[currentInstruction][1])>0 :
			return 0
			
		elif diccInstrucctionsParsed[currentInstruction][0] == "jmp" and int(diccInstrucctionsParsed[currentInstruction][1])<=0 :
			return execBootProgramRepes(diccInstrucctionsParsed, currentInstruction+(int(diccInstrucctionsParsed[currentInstruction][1])), accValue, visitedInstrucctions)

main()