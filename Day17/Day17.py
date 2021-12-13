#!/usr/bin/python3
# -*- coding: utf-8 -*-



def main():


	energy_matrix:list = getInputData('input')

	simulate3DActiveNodes(getActiveNodes(energy_matrix,3))
	simulate4DActiveNodes(getActiveNodes(energy_matrix,4))



###################################################################
###########				GET INPUT		###########################
###################################################################

def getInputData(input_name:str):
	
	raw_data:list = readInputData(input_name)
	return parseInputData(raw_data)



def readInputData(input_name:str):

	data:list = []
	file = open(input_name,"r")

	for line in file:
		data.append(line.strip())
	return data

def parseInputData(raw_data:list):

	data_parsed:list = []

	for line in raw_data:
		data_parsed.append(list(line))

	return data_parsed


###################################################################



###################################################################
#################		COMMON  			#######################
###################################################################

def simulateCicle(active_nodes_str:list, dimensions:int):

	new_active_nodes:list = []
	inactive_nodes_count:dict = {}

	for node_str in active_nodes_str:

		active_neighbours_counter:int = 0
		neighbour_nodes_str = []

		if (dimensions == 3): neighbour_nodes_str = [nodeToString(neighbour_str) for neighbour_str in getNeighboursNodes3D(stringToNode(node_str))]
		elif(dimensions == 4): neighbour_nodes_str = [nodeToString(neighbour_str) for neighbour_str in getNeighboursNodes4D(stringToNode(node_str))]

		for neighbour_str in neighbour_nodes_str:

			if (neighbour_str in active_nodes_str):
				active_neighbours_counter = active_neighbours_counter + 1

			elif ((neighbour_str not in active_nodes_str) and (neighbour_str not in inactive_nodes_count)):
				inactive_nodes_count[neighbour_str] = 1

			elif ((neighbour_str not in active_nodes_str) and (neighbour_str in inactive_nodes_count)):
				inactive_nodes_count[neighbour_str] = inactive_nodes_count[neighbour_str] + 1


		if (active_neighbours_counter == 2 or active_neighbours_counter == 3):
			new_active_nodes.append(node_str)

	for key_inactive in inactive_nodes_count.keys():

		if (inactive_nodes_count[key_inactive] == 3):
			new_active_nodes.append(key_inactive)

	return new_active_nodes


def getActiveNodes(energy_matrix:list, dimensions:int):
	
	active_nodes:list = []

	for index_x in range(0,len(energy_matrix)):
		for index_y in range(0,len(energy_matrix[index_x])):

			if(energy_matrix[index_x][index_y] == "#"):
				active_nodes .append([index_x,index_y]+[0]*(dimensions-2))

	return active_nodes


def nodeToString(node:list):

	return ','.join(map(str,node))

def stringToNode(node:str):
	return [int(coordinate) for coordinate in node.split(",")]

###################################################################



###################################################################
#################		PART ONE			#######################
###################################################################

def simulate3DActiveNodes(active_nodes:list):

	active_nodes_str = [nodeToString(node) for node in active_nodes]

	for cicle in range(0,6):
		active_nodes_str = simulateCicle(active_nodes_str,3)
	print(len(active_nodes_str))



def getNeighboursNodes3D(node:list):

	neighbour_nodes:list = []
	for index_x in range(node[0]-1, node[0]+2):
		for index_y in range(node[1]-1, node[1]+2):
			for index_z in range(node[2]-1, node[2]+2):
				neighbour_nodes.append([index_x, index_y, index_z])

	neighbour_nodes.remove(node)
	return neighbour_nodes

###################################################################

###################################################################
#################		PART TWO			#######################
###################################################################

def simulate4DActiveNodes(active_nodes:list):

	active_nodes_str = [nodeToString(node) for node in active_nodes]

	for cicle in range(0,6):
		active_nodes_str = simulateCicle(active_nodes_str,4)
	print(len(active_nodes_str))



def getNeighboursNodes4D(node:list):

	neighbour_nodes:list = []
	for index_x in range(node[0]-1, node[0]+2):
		for index_y in range(node[1]-1, node[1]+2):
			for index_z in range(node[2]-1, node[2]+2):
				for index_w in range(node[3]-1, node[3]+2):
					neighbour_nodes.append([index_x, index_y, index_z, index_w])

	neighbour_nodes.remove(node)
	return neighbour_nodes

###################################################################

if __name__ == '__main__':
	main()
