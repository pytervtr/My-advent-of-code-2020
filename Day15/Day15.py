import re

def main():

	input = "15,5,1,4,7,0"
	dict = parseEntry(input)
	elfGameImprove(dict, 2020)	

	dict = parseEntry(input)
	elfGameImprove(dict, 30000000)

def parseEntry(input):

	roundDictionary = {}

	if input.find(",\n") == -1:
		input = input +","

	for spokenNumberIndex in range(input.count(",")):

		key_spokenNumber = int(input[:input.index(",")])

		roundDictionary[key_spokenNumber] = [spokenNumberIndex+1]

		input = input[input.index(",")+1:]

	return roundDictionary

def elfGameImprove(roundDictionary, max_rounds):

	lastSpokenNumber_key = [key for key in roundDictionary.keys() if roundDictionary[key] == max(roundDictionary.values())][0]

	value = 0

	for round in range(len(roundDictionary)+1, max_rounds+1):

		if (len(roundDictionary[lastSpokenNumber_key]) == 1 
			and 0 in roundDictionary.keys()):#numero nuevo

			value = roundDictionary[0][0]

			roundDictionary[0] = [round,value]

			lastSpokenNumber_key = 0

		elif (len(roundDictionary[lastSpokenNumber_key]) == 1 
			and 0 not in roundDictionary.keys()):#numero nuevo

				roundDictionary[0] = [round]
				lastSpokenNumber_key = 0


		elif (len(roundDictionary[lastSpokenNumber_key]) == 2):


			value = roundDictionary[lastSpokenNumber_key][0] - roundDictionary[lastSpokenNumber_key][1]

			if value in roundDictionary.keys():

				roundDictionary[value] = [round, roundDictionary[value][0]]


			elif value not in roundDictionary.keys():

				roundDictionary[value] = [round]

			lastSpokenNumber_key = value

		
		#if(round % 1000000 == 0) :
		#	print(round)
	
	print(lastSpokenNumber_key,"\n")




main()
