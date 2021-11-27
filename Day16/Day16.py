#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import numpy

def main():

	#print(readData("input")[0])
	dictionary = getIntputData()
	#print(dictionary)
	print(getOperationValue(dictionary))
	print(getDepartureValue(dictionary))

###################################################################
###########				GET INPUT		###########################
###################################################################
def getIntputData():

	return parseInputData(readData("input"))

def readData(input:str):

	inputData:str = []
	file = open(input,"r")

	for line in file:
		if(line.strip() != ""):
			inputData.append(line.strip())

	return inputData

def parseInputData(inputData:list):

	parseInput:dict = {}

	for line in inputData:

		if(":" in line and line.index(":")+1 != len(line)):#si es una entrada uni linea

			key = line[:line.index(":")]
			value_tmp = re.split(r'or|-',line[line.index(":")+1:].replace(" ",""))

			iterator = iter(value_tmp)
			parseInput[key]=[[int(val),int(next(iterator))] for val in iterator]

		elif(":" in line and line.index(":")+1 == len(line)):#si es el inicio de una entrada multi linea
			
			key = line[:line.index(":")]
			parseInput[key] = []

		elif (":" not in line): # si es la continauacion de uan estrada multilinea

			parseInput[key] = parseInput[key] + [[ int(ticket) for ticket in line.split(",")]]


	return parseInput

###################################################################

###################################################################
#################		PART ONE			#######################
###################################################################


def getOperationValue(dictionary:dict):

	return sum(getInvalidTickets(dictionary.copy()))

def getInvalidTickets(dictionary:list):

	result:list = []
	flag:bool = False

	nearby_tickets:list = sum(dictionary['nearby tickets'],[])
	dictionary.pop('your ticket')
	dictionary.pop('nearby tickets')




	for ticket in nearby_tickets:
		for value in sum(dictionary.values(),[]):

			if isInBound(value, ticket):
				flag = True
				break

		if flag == False:
			result.append(ticket)
		flag = False

	return result

###################################################################

###################################################################
#################		PART TWO			#######################
###################################################################

def getDepartureValue(dictionary:dict):

	valid_tickets:dict = removeInvalidTickets(dictionary)
	definitive_positions:dict = getOrderTicketFidels(valid_tickets.copy())
	return numpy.prod(getSpecificValues(definitive_positions,dictionary['your ticket'][0],'departure'))

def removeInvalidTickets(dictionary:dict):

	invalid_tickets:list = getInvalidTickets(dictionary.copy())
	new_tickets:list = []

	for possible_incorrect_ticket in dictionary['nearby tickets']:

		if not [ticket for ticket in invalid_tickets if ticket in possible_incorrect_ticket]:
			new_tickets.append(possible_incorrect_ticket)

	dictionary['nearby tickets'] = new_tickets

	return dictionary


def getOrderTicketFidels(valid_dictionary:dict):

	ticket_fields:list = list(numpy.transpose(valid_dictionary['nearby tickets']))
	indexes_list:list = []

	valid_dictionary.pop('your ticket')
	valid_dictionary.pop('nearby tickets')


	for key in valid_dictionary.keys():
		indexes_list.append([key]+getPositionKeys(ticket_fields,valid_dictionary[key]))

	return filterPositions(indexes_list) 


def getPositionKeys(ticket_fields:list, key_ranges:list):

	matches:int = 0
	correct_indexes:list = []

	for index_row in range(len(ticket_fields)):
		for index_column in range(len(ticket_fields[index_row])):

			if [1 for range_pair in key_ranges if isInBound(range_pair, ticket_fields[index_row][index_column])]:
				matches = matches +1

			else:
				break

		if matches == len(ticket_fields[index_row]):
			correct_indexes.append(index_row)

		matches = 0

	return correct_indexes


def filterPositions(indexes_list:list):

	definitive_positions:dict = {}
	already_used:list = []

	for field_indexes in sorted(indexes_list,key=len):
		key = field_indexes[0]
		field_indexes.remove(key)

		definitive_positions[key] = [index for index in field_indexes if index not in already_used] [0]
		already_used.append(definitive_positions[key])

	return definitive_positions


def getSpecificValues(definitive_positions:dict, your_ticket:list, specific_key:str):

	specific_key_values:list = []

	for key in definitive_positions.keys():

		if specific_key in key:
			specific_key_values.append(your_ticket[definitive_positions[key]])

	return specific_key_values

###################################################################

###################################################################
#################		 COMMON 			#######################
###################################################################

def isInBound(ranges:list, value:int):
	return (ranges[0]<=value and ranges[1]>=value)


###################################################################


if __name__ == '__main__':
	main()