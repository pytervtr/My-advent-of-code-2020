import math
import numpy

def main():

	inputData = readInputFile()

	###################################################
	#----------			VERSION 1			----------#
	###################################################

	print(updateMemValues(inputData))

	###################################################
	#----------			VERSION 2			----------#
	###################################################

	print(updateMemAddress(inputData))



def readInputFile():
	file = open("input","r")

	inputData = []

	current_mask = ""
	current_mem_pos = ""
	current_mem_val = ""

	for line in file:
		if("mask" in line):
			current_mask = line[line.index("=")+2:-1]
		elif ("mem" in line):
			current_mem_pos = line[line.index("[")+1:line.index("]")]
			current_mem_val = line[line.index("=")+2:].strip()
		
			inputData.append([current_mask,current_mem_pos,current_mem_val])
			
	return inputData


def updateMemValues(inputData):

	mem = {}

	for line in inputData:
		current_mask = line[0]
		current_mem_pos = line[1]
		current_mem_val =  decimalToBinary(line[2],len(line[0]))
	
		current_mask = list(current_mask)
		current_mem_pos = int(current_mem_pos)
		current_mem_val = list(current_mem_val)

		for digitPosition in range(len(current_mask)):
			if current_mask[digitPosition] != 'X':
				current_mem_val [digitPosition] = current_mask[digitPosition]

		current_mem_val = ''.join(current_mem_val)

		mem[current_mem_pos] = binaryToDecimal(current_mem_val)
	
	return resultSum(mem)


def updateMemAddress(inputData):

	mem = {}

	for line in inputData:
		current_mask = line[0]
		current_mem_pos = decimalToBinary(line[1], len(current_mask))
		current_mem_val = line[2]

		current_mask = list(current_mask)
		current_mem_pos = list(current_mem_pos)
		current_mem_val = int(current_mem_val)

		new_mems_pos = ['']

		for digitPosition in range(len(current_mem_pos)):
			if current_mask[digitPosition] == 'X':
				new_mems_pos = [i+'0' for i in new_mems_pos] + [i+'1' for i in new_mems_pos]

			elif current_mask[digitPosition] == '1':
				new_mems_pos = [i+'1' for i in new_mems_pos]

			elif current_mask[digitPosition] == '0':
				new_mems_pos = [i+current_mem_pos[digitPosition] for i in new_mems_pos] 

				
		for binaryAddressIndex in range(len(new_mems_pos)):
			new_mems_pos[binaryAddressIndex] = binaryToDecimal(new_mems_pos[binaryAddressIndex])

		print(new_mems_pos)

		for decimalAddres in new_mems_pos:
			mem[decimalAddres] = current_mem_val

	print(mem)

	return resultSum(mem)


def decimalToBinary(decimalNumber, lengthMask):
	binaryNumber = ""
	decimalNumber = int(decimalNumber)

	quotient = 0
	remainder = 0

	while(decimalNumber != 1 and decimalNumber != 0):
		quotient = decimalNumber//2
		remainder = int(decimalNumber%2)

		decimalNumber = quotient
		binaryNumber = binaryNumber + str(remainder)

	binaryNumber = binaryNumber + str(quotient)

	return extendSign(binaryNumber[::-1], lengthMask)


def extendSign(binaryNumber, lengthMask):
	return "0"*(lengthMask-len(binaryNumber))+binaryNumber

def binaryToDecimal(binaryNumber):
	decimalNumber = 0
	length = len(binaryNumber)-1

	for digit in binaryNumber:
		decimalNumber = decimalNumber + int(digit)*pow(2,length)
		length-=1

	return decimalNumber	

def resultSum(mem):
	sumAll = 0

	for element in mem.keys():
		sumAll = sumAll + mem[element]

	return sumAll





main()
