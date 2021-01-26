import array
import time
from itertools import combinations
import sys
import numpy as np

def main():
	
	puzzle = []
	file = open("inputDay10","r")

	for line in file:
		puzzle.append(int(line.rstrip("\n")))

	puzzle = addOtherVoltage(puzzle)
	puzzle = sorted(puzzle)

	countAdapters(puzzle)		#funcion primera parte 
	checkCombinations(puzzle)	#funcion segunda parte


##########################################################################
#Busca el numero de adaptadores de cada tipo, de menor a mayor potencial #
#que permitan llegar al maximo potencial								 #
##########################################################################
	
def addOtherVoltage(puzzle):
	puzzle.append(max(puzzle)+3)
	puzzle.append(0)
	return puzzle
def countAdapters(puzzle):
	adapter1J=0
	adapter2J=0
	adapter3J=0

	visitedRatings = []
	counter = 0
	error = 0

	for jRating in puzzle:

		if jRating+1 in puzzle and jRating+1 not in visitedRatings:
			adapter1J += 1
			visitedRatings .append(jRating+1)
			counter +=1

		elif jRating+2 in puzzle and jRating+2 not in visitedRatings:
			adapter2J += 1
			visitedRatings .append(jRating+2)
			counter +=1		
		
		elif jRating+3 in puzzle and jRating +3 not in visitedRatings:
			adapter3J += 1
			visitedRatings .append(jRating+3)
			counter +=1
		elif jRating != puzzle[len(puzzle)-1]:
			return -1
	print()
	print(adapter1J*adapter3J)
	print()
#########################################################################
#recorre todos los elementos buscando el actual +1 o la menor distancia #
#recorre todos los elementos buscando el actual +2 o la menor distancia #
#recorre todos los elementos buscando el actual +3 o la menor distancia # 
#########################################################################
def checkCombinations(puzzle):
	count = 0
	dictComplete = dict.fromkeys(puzzle,0)
	count = countCombinations_withoutPath(puzzle, puzzle[0],dictComplete)
	print()
	print(count)
	print()

def countCombinations_withoutPath(puzzle, currentValue,dictComplete):

	posibles = [1,2,3]
	count = 0

	if puzzle[len(puzzle)-1] == currentValue:
		dictComplete[currentValue] = 1
		return 1


	for voltage in posibles:
		if currentValue + voltage in puzzle and dictComplete[currentValue+voltage]==0:				
			dictComplete[currentValue+voltage] = countCombinations_withoutPath(puzzle, currentValue+voltage,dictComplete)
			count = dictComplete[currentValue+voltage]+count

		elif currentValue + voltage in puzzle and dictComplete[currentValue+voltage]!=0:				
			count = dictComplete[currentValue+voltage]+count			

	return count

'''
def countCombinations_withPath(puzzle, currentValue, tempPath):

	posibles = [1,2,3]

	visited =[]
	tempPath.append(currentValue)
	possiblePath=[]

	if puzzle[len(puzzle)-1] == currentValue:
		return [tempPath]


	for voltage in posibles:
		if currentValue + voltage in puzzle:			
			
			possiblePath = countCombinations(puzzle, currentValue+voltage, tempPath)		

			if type(possiblePath[0]) is int and puzzle[len(puzzle)-1] in possiblePath:
				#print("primero",currentValue)
				visited[len(visited)-1].append(possiblePath.copy())

			elif type(possiblePath[0]) is list :

				for camino in possiblePath:
					visited.append(camino.copy())

			possiblePath=[]
			tempPath.pop(len(tempPath)-1)

	return visited
'''

main()