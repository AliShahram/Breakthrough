#Part 2 of the lab
import random
from transition import *


#Utility function takes a board state as input
#and returns a value between 1 and 10 indicating
#how desirable the state is 


#Evasive uses the number of pieces remaining for the player
#and values it based on how many is left

def evasive(player, input_state):
	p_remaining = 0.  #Number of pieces remaining
	
	for row in input_state:		#Check which player it is and calculate the number
		for column in row:			#of pieces remaining for them
			if player == "X":
				if column == "X":
					p_remaining += 1
			if player == "O":
				if column == "O":
					p_remaining += 1

	percentange = random.uniform(0,1)	#Generates random number between 0-1
	Num = round(percentange , 2)		#round it down to one decimal
	utility = p_remaining + Num         #utility is evasive
	return utility

	


def conqueror(player, input_state):
	p_remaining = 0.  #Number of pieces remaining
	
	for row in input_state:		#Check which player it is and calculate the number
		for column in row:			#of pieces remaining for them
			if player == "X":
				if column == "O":
					p_remaining += 1
			if player == "O":
				if column == "X":
					p_remaining += 1

	percentange = random.uniform(0,1)	#Generates random number between 0-1
	Num = round(percentange , 2)		#round it down to one decimal
	utility = (0 - p_remaining) + Num         #utility is conquerer
	return utility





def winningscore(player, state):
	board = Board(state, player)
	winningvalue = 200
	if player == "X":
		if board.terminal_state() == "X":
			return winningvalue 
		elif board.terminal_state() == "O":
			return (-1) * winningvalue
		else:
			return 0
	elif player == "O":
		if board.terminal_state() == "O":
			return winningvalue
		elif board.terminal_state() == "X":
			return (-1) * winningvalue
		else:
			return 0

	else:
		return 0




def myscore (player, input_state):
	Num_pieces = 0
	player_X = []
	player_O = []
	total = 0


	row_num = 0
	for row in input_state:
		row_num = row_num + 1
		column_num = 0
		for column in row:
			column_num = column_num + 1
			piece = (row_num - 1, column_num - 1)
			if column == "X":
				player_X.append(piece)
			if column == "O":
				player_O.append(piece)
	
	if player == "X":
		for pos in player_X:
			total = pos[0] + total
		Num_player = len(player_X)

		return Num_player + total + winningscore(player, input_state)

	elif player == "O":
		for pos in player_O:
			total = pos[0] + total
		Num_player = len(player_X)
		return Num_player + (row_num - total) + winningscore(player, input_state)


def enemyscore(player, input_state):
	Num_pieces = 0
	player_X = []
	player_O = []
	total = 0

	row_num = 0
	for row in input_state:
		row_num = row_num + 1
		column_num = 0
		for column in row:
			column_num = column_num + 1
			piece = (row_num - 1, column_num - 1)
			if column == "X":
				player_X.append(piece)
			if column == "O":
				player_O.append(piece)

	if player == "X":
		for pos in player_O:
			total = pos[0] + total
		Num_player = len(player_X)
		return Num_player + (row_num - total)  + winningscore("O", input_state)

	elif player == "O":
		for pos in player_X:
			total = pos[0] + total
		Num_player = len(player_X)
		return Num_player + total + winningscore("X", input_state)


def house_lannister(player, input_state):
	result = 2 * (myscore(player, input_state) - 1) * enemyscore(player, input_state)
	percentange = random.uniform(0,1)	#Generates random number between 0-1
	Num = round(percentange , 2)
	result = result + Num
	return result


def house_stark(player, input_state):
	result = 1 * (myscore(player, input_state) - 2) * enemyscore(player, input_state)
	percentange = random.uniform(0,1)	#Generates random number between 0-1
	Num = round(percentange , 2)
	result = result + Num
	return result



"""
state = [["X","X", "X"], [".",".", "."], ["O","O", "O"]]
result = house_stark("X", state)
print(result)
"""
