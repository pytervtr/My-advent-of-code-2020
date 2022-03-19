#!/usr/bin/python3
# -*- coding: utf-8 -*-

import operator
import re

class NestedOperations:

	def __init__(self, first_operand, sign_operator:str, second_operand):
		self.first_operand = first_operand
		self.sign_operator = sign_operator
		self.second_operand = second_operand


	def executeOperation(self):
		signos:dict = {"+":operator.add,"-":operator.sub,'*':operator.mul,"/":operator.floordiv}
		result:int = 0

		if ( (type (self.first_operand) is not NestedOperations) and (type (self.second_operand) is not NestedOperations)):
			result = signos[self.sign_operator](self.first_operand,self.second_operand)

		elif ( (type (self.first_operand) is NestedOperations) and (type (self.second_operand) is not NestedOperations)):
			result = signos[self.sign_operator](self.first_operand.executeOperation(),self.second_operand)

		elif ( (type (self.first_operand) is not NestedOperations) and (type (self.second_operand) is NestedOperations)):
			result = signos[self.sign_operator](self.first_operand,self.second_operand.executeOperation())

		elif ( (type (self.first_operand) is NestedOperations) and (type (self.second_operand) is NestedOperations)):
			result = signos[self.sign_operator](self.first_operand.executeOperation(),self.second_operand.executeOperation())

		return result

class Day18:




	def firstPart(self):
		raw_operations:list = self.readFile()
		estructured_operations:list = self.parseRawOperations(raw_operations)

		return self.executeCalculationOrder(estructured_operations)


	def secondPart(self):
		raw_operations:list = self.readFile()
		raw_priority_operations:list = self.setOperationPriority(raw_operations, '+')
		estructured_operations:list = self.parseRawOperations(raw_priority_operations)

		return self.executeCalculationOrder(estructured_operations)


	def setOperationPriority(self, raw_operations,symbol_priority):
		raw_priority_operations:list = []
		tmp_priority_operations:list = []



		for operation in raw_operations:
			operation = operation.replace("(","( ")
			operation = operation.replace(")"," )")

			operation = operation.split()

			operation_dict:dict = {}
			sorted_keys:list = []			

			for parenthesis_count in range(operation.count(")")):
				begin:int = len(operation) - operation[::-1].index('(')-1
				end:int = operation[begin:].index(')')+begin

				sub_operation = operation[begin+1:end]

				symbol_result = self.appendParenthesisToSymbol(sub_operation, operation_dict, sorted_keys, symbol_priority)

				operation_dict.update(symbol_result[1])
				sorted_keys = symbol_result[2] 
				sub_operation = symbol_result[0]

				key = "operation"+str(len(operation_dict.keys()))

				operation_dict[key] = ["("] + sub_operation +[")"]
				sorted_keys = [key] + sorted_keys	

				operation = operation[:begin] + [key] + operation[end+1:]

				

			symbol_result = self.appendParenthesisToSymbol(operation, operation_dict, sorted_keys, symbol_priority)

			operation_dict.update(symbol_result[1])
			sorted_keys = symbol_result[2] 
			sub_operation = symbol_result[0]
			
			key = "operation"+str(len(operation_dict.keys()))
			previous_key = "operation"+str(len(operation_dict.keys())-1)

			operation_dict[key] = ['('] + sub_operation + [')']#ESTA COSA ES UNA MIERDA TODO

			sorted_keys = [key] + sorted_keys	

			operation = [key]
			tmp_priority_operations.append([operation, operation_dict, sorted_keys])


		for operation_line in tmp_priority_operations:
			operation = operation_line[0]
			for key in operation_line[2]:
				index = operation.index(key)

				if(len(operation_line[1][key])==3):
					operation = operation[:index] + [operation_line[1][key][1]] + operation[index+1:]

				elif(len(operation_line[1][key])!=3):
					operation = operation[:index] + operation_line[1][key] + operation[index+1:]

			operation = " ".join(operation)

			operation = operation.replace("( ","(")
			operation = operation.replace(" )",")")

			raw_priority_operations.append(operation)
		return raw_priority_operations


	def appendParenthesisToSymbol(self, sub_operation, operation_dict, sorted_keys, symbol_priority):
		for simbol_count in range(sub_operation.count(symbol_priority)):
			index:int = len(sub_operation) - sub_operation[::-1].index(symbol_priority) -1

			key = "operation"+str(len(operation_dict.keys()))

			operation_dict[key] = ['(',sub_operation[index-1],sub_operation[index],sub_operation[index+1],')']
			sorted_keys = [key] + sorted_keys
			sub_operation = sub_operation[:index-1] + [key] + sub_operation[index+2:]

		return [sub_operation, operation_dict, sorted_keys]

	def validPriorityIndex(self,operation_list, symbol_precedence):
		valid_index = operation_list.index(symbol_precedence)
		if(operation_list.count(symbol_precedence) == 1 and ("(" == operation_list[valid_index+1])):
			return -100

		elif(operation_list.count(symbol_precedence) != 1 and "(" == operation_list[valid_index+1]):
			valid_index = (self.validPriorityIndex(operation_list[valid_index+2:], symbol_precedence)+valid_index+2)

		return valid_index


	def readFile(self):
		file = open("input", "r")
		data:list = []

		for line in file:
			data.append(line.strip())

		return data

	def parseRawOperations(self, raw_operations):
		parsedOperations:list = []		
		varDicts:dict ={}


		for operation in raw_operations:
			for count_priorities in range(operation.count("(")):

				begin:int = operation.rfind('(')+1
				end:int = operation[begin:].find(')')+begin

				name:str = "nestedOp"+str(len(varDicts.keys()))
				value = operation[begin:end]

				varDicts[name]=self.simplifyOperation(value, varDicts)

				operation = operation[:begin-1] + name +operation[end+1:]

			if(len(operation.split())!=1):
				parsedOperations.append(self.simplifyOperation(operation, varDicts))
			elif(len(operation.split())==1):
				parsedOperations.append(varDicts[operation])
				
		return parsedOperations

	def simplifyOperation(self, operation, varDicts):
		splited_operation:list = operation.split(" ")

		first_operand = splited_operation[0]
		operator:str = ""
		second_operand = ""

		iterator = iter(splited_operation[1:])
		for operand in iterator:

			operator = operand


			second_operand = next(iterator)



			if((type(first_operand) is not NestedOperations) and (not first_operand.isdigit())):
				first_operand = varDicts[first_operand]

			elif((type(first_operand) is not NestedOperations) and (first_operand.isdigit())):
				first_operand = int(first_operand)


			if((type(second_operand) is not NestedOperations) and (not second_operand.isdigit())):
				second_operand = varDicts[second_operand]

			elif((type(second_operand) is not NestedOperations) and ( second_operand.isdigit())):
				second_operand = int(second_operand)

			first_operand = NestedOperations(first_operand, operator, second_operand)
			
		return first_operand


	def executeCalculationOrder(self, parsedOperations):

		result = 0

		for operation in parsedOperations:
			result = result + operation.executeOperation()

		print("")
		print(result)
		print("")


	def __init__(self):
		self.firstPart()
		self.secondPart()


if __name__ == "__main__":
	Day18()
