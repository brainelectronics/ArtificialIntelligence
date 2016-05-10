#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
In this exercise you are going to implement part of a propositional system for 
a Pacman Agent. Given the limitations of propositional logic, it is going to 
be a very simple system, but it should serve to illustrate the concept.

The point of this exercise is to use propositional logic lo localize the ghost 
in a 4x4 map. This is made difficult by the fact that Pacman can not see 
further than one step in the grid, so he does not have access to the full 
state, but his perception only consists of a chill when he is in a square 
adjacent to a ghost.

For this exercise, we are only interesed in one single piece of 
information - that is, if it is safe for Pacman to move to the square (1, 2) 
based on the imformation he has already perceived. This information is 
represented in the state, which contains a label for each square of the grid, 
which is one of C_i_j if the square (i,j) is chilly, -C_i_j if there was no 
chill, and NV_i_j if Pacman hasn't been there yet. This is an example state:

['-C_0_0',
 'NV_0_1',
 'NV_0_2',
 '-C_0_3',
 'NV_1_0',
 'C_1_1',
 'NV_1_2',
 'C_1_3',
 '-C_2_0',
 'NV_2_1',
 'C_2_2',
 '-C_2_3',
 '-C_3_0',
 'NV_3_1',
 'NV_3_2',
 '-C_3_3']

The state can be visualized rudimentarily with the show_state function given 
below - for this example state it looks like this:

[['0', '.', '.', '0'],	[(0,0), (0,1), (0,2), (0,3)],
 ['.', 'C', 'G', 'C'],	[(1,0), (1,1),  ?G? , (1,3)],
 ['0', '.', 'C', '0'],	[(2,0), (2,1), (2,2), (2,3)],
 ['0', '.', '.', '0']]	[(3,0), (3,1), (3,2), (3,3)],

Please provide a function that, based on this state description, returns one of 
the labels Safe_1_2, Unsafe_1_2 or Ghost_1_2, which tell if there cannot be a 
ghost, there could maybe be a ghost, or there certainly is a ghost, for the 
square (1, 2). In the example, the return value should be Ghost_1_2, because 
from the three chilly squares surrounding the target square, it is clear that 
the ghost has to be there.

Your solution should work on propositional level, i.e. you should not have to 
parse the positions out of the state symbols, but write rules that work on the 
state directly.
"""
"""
testState = [
'-C_0_0', 'NV_0_1', 'NV_0_2', '-C_0_3',
'NV_1_0', 'C_1_1', 'NV_1_2', 'C_1_3',
'-C_2_0', 'NV_2_1', 'C_2_2', '-C_2_3',
'-C_3_0', 'NV_3_1', 'NV_3_2', '-C_3_3']

testState2 = [
'NV_0_0', 'NV_0_1', 'NV_0_2', 'NV_0_3',
'-C_1_0', 'NV_1_1', 'NV_1_2', 'NV_1_3',
'NV_2_0', 'NV_2_1', 'NV_2_2', 'NV_2_3',
'C_3_0', 'NV_3_1', 'NV_3_2', 'NV_3_3']

testState3 = [
'NV_0_0', 'NV_0_1', 'NV_0_2', 'NV_0_3',
'NV_1_0', 'NV_1_1', 'NV_1_2', 'NV_1_3',
'NV_2_0', 'NV_2_1', 'NV_2_2', 'NV_2_3',
'NV_3_0', 'NV_3_1', 'NV_3_2', 'NV_3_3']

testState4 = [
'NV_0_0', 'NV_0_1', 'C_0_2', 'NV_0_3',
'NV_1_0', 'NV_1_1', 'NV_1_2', 'C_1_3',
'NV_2_0', 'NV_2_1', 'NV_2_2', 'NV_2_3',
'NV_3_0', 'NV_3_1', 'NV_3_2', 'NV_3_3']
"""
someTestStates = [
['NV_0_0', 'NV_0_1', 'NV_0_2', 'NV_0_3', 'NV_1_0', 'C_1_1', 'NV_1_2', 'NV_1_3', 'NV_2_0', 'NV_2_1', 'C_2_2', 'NV_2_3', 'NV_3_0', 'NV_3_1', 'NV_3_2', 'NV_3_3'],
['NV_0_0', 'NV_0_1', 'NV_0_2', 'NV_0_3', 'NV_1_0', 'NV_1_1', 'NV_1_2', 'NV_1_3', 'NV_2_1', 'NV_2_0', 'NV_2_2', 'NV_2_3', 'NV_3_0', 'NV_3_2', 'NV_3_1', 'NV_3_3'],
['C_0_0', 'NV_0_1', 'NV_0_2', 'NV_0_3', 'NV_1_0', 'NV_1_1', 'NV_1_2', 'NV_1_3', 'NV_2_1', 'NV_2_0', 'NV_2_2', 'NV_2_3', 'NV_3_0', 'NV_3_2', 'NV_3_1', 'NV_3_3'],
['-C_0_0', 'NV_0_1', 'NV_0_2', 'NV_0_3', 'NV_1_0', 'NV_1_1', 'NV_1_2', 'C_1_3', 'NV_2_1', 'NV_2_0', 'NV_2_2', 'NV_2_3', 'NV_3_0', 'NV_3_2', 'NV_3_1', 'NV_3_3'],
['NV_0_0', '-C_0_1', 'NV_0_2', 'NV_0_3', '-C_1_0', 'C_1_1', 'NV_1_2', 'NV_1_3', '-C_2_1', 'NV_2_0', 'NV_2_2', 'NV_2_3', 'NV_3_0', 'NV_3_2', 'NV_3_1', '-C_3_3'],
['NV_0_0', 'NV_0_1', 'C_0_2', 'NV_0_3', '-C_1_0', '-C_1_1', '-C_1_2', 'C_1_3', 'NV_2_0', 'NV_2_1', '-C_2_2', '-C_2_3', '-C_3_0', '-C_3_1', '-C_3_2', '-C_3_3'],
['-C_0_0', 'NV_0_1', '-C_0_2', '-C_0_3', 'C_1_0', '-C_1_1', '-C_1_2', '-C_1_3', 'NV_2_0', 'C_2_1', '-C_2_2', '-C_2_3', 'C_3_0', 'NV_3_1', '-C_3_2', '-C_3_3'],
['-C_0_0', 'NV_0_1', '-C_0_2', '-C_0_3', 'NV_1_0', 'NV_1_1', '-C_1_2', 'NV_1_3', 'C_2_0', 'NV_2_1', 'C_2_2', 'NV_2_3', '-C_3_0', 'NV_3_1', '-C_3_2', '-C_3_3'],
['-C_0_0', '-C_0_1', 'NV_0_2', '-C_0_3', 'NV_1_0', 'C_1_1', '-C_1_2', 'NV_1_3', 'C_2_0', 'NV_2_1', 'NV_2_2', '-C_2_3', '-C_3_0', 'C_3_1', '-C_3_2', '-C_3_3'],
['NV_0_0', 'C_0_1', 'NV_0_2', '-C_0_3', 'C_1_0', 'NV_1_1', '-C_1_2', 'NV_1_3', '-C_2_0', '-C_2_1', 'NV_2_2', 'NV_2_3', 'NV_3_0', '-C_3_1', 'NV_3_2', '-C_3_3'],
['-C_0_0', 'C_0_1', '-C_0_2', '-C_0_3', 'C_1_0', 'NV_1_1', 'NV_1_2', '-C_1_3', '-C_2_0', 'NV_2_1', 'NV_2_2', 'NV_2_3', 'NV_3_0', '-C_3_1', '-C_3_2', '-C_3_3']
]

import pprint
def show_state(state, ghost_pos=None):
	"""
	Show the state graphically, and the position of the ghost, if it is known
	"""
	chars = {'C': 'C', 
			 '-C': '0',
			 'NV': '.'}
	
	ss = [range(4) for _ in range(4)]
	for s in state:
		c, i, j = s.split('_')
		ss[int(i)][int(j)] = chars[c]
	if ghost_pos:
		ss[ghost_pos[0]][ghost_pos[1]] = 'G'

	pprint.pprint(ss)
	return ss

"""
show_state returns:
[['0', '.', '.', '0'],
 ['.', 'C', '.', 'C'],
 ['0', '.', 'C', '0'],
 ['0', '.', '.', '0']]

"""

def is_1_2_safe(state):
	"""
	a function that determines in a propositional way if it safe to move to 
	the (1, 2) square.

	Safe_1_2 == no ghost
	Unsafe_1_2 == maybe a ghost
	Ghost_1_2 == a ghost
	"""
	# orginal
	# if 1:
	# 	return 'Safe_1_2'	# Safe_1_2 == no ghost
	# elif 2:
	# 	return 'Ghost_1_2'	# Ghost_1_2 == a ghost
	# else:
	# 	return 'Unsafe_1_2'	# Unsafe_1_2 == maybe a ghost

	newDict = dict.fromkeys(range(0,16), 0)	# generate new dict with keys 0-16 and values 0
	chillyList = []
	problemMatrix = show_state(state=state, ghost_pos=None)
	for lineCounter, line in enumerate(problemMatrix):
		for elementCounter, element in enumerate(line):
			currentPosition = lineCounter*4+elementCounter
			topPosition = (lineCounter-1)*4+elementCounter
			bottomPosition = (lineCounter+1)*4+elementCounter
			leftPosition = lineCounter*4+(elementCounter-1)
			rightPosition = lineCounter*4+(elementCounter+1)

			if 'C' in element:
				theInsertValue = 10
				newDict[currentPosition] =  -999

				if (lineCounter-1) >= 0:	# there is a line above available
					newDict[topPosition] += theInsertValue
				if (lineCounter+1) < 4:		# there is a line underneath available
					newDict[bottomPosition] += theInsertValue
				if (elementCounter-1) >= 0:	# there is a left row available
					newDict[leftPosition] += theInsertValue
				if (elementCounter+1) < 4:	# there is a right row available
					newDict[rightPosition] += theInsertValue
			elif '0' in element:
				theInsertValue = -10
				newDict[currentPosition] =  -555

				if (lineCounter-1) >= 0:	# there is a line above available
					newDict[topPosition] += theInsertValue
				if (lineCounter+1) < 4:		# there is a line underneath available
					newDict[bottomPosition] += theInsertValue
				if (elementCounter-1) >= 0:	# there is a left row available
					newDict[leftPosition] += theInsertValue
				if (elementCounter+1) < 4:	# there is a right row available
					newDict[rightPosition] += theInsertValue
			else:	# no 'C' or '0'
				theInsertValue = 0
				pass
    # '''
    # debug
	for x in range(16):
		if x%4 == 0:
			print "\n",
		print "%s," %newDict[x],
    # '''

	print "\n"
	ghostList = [element for element, pos in newDict.items() if pos > 0]
	print "ghosts at id %s" %ghostList
	mostSure = max(newDict, key=newDict.get)

	ghostPos = [(seems/4, ((seems+1)%4)-1) for seems in ghostList ]
	print "ghostPos %s" %ghostPos

    # a ghost at (1,2) and only one ghost detected
    # OR
    # a ghost at (1,2) and the most likely is at (1,2)
	if (1,2) in ghostPos and (len(ghostPos) == 1 or ((mostSure/4, ((mostSure+1)%4)-1) == (1,2))):
		return 'Ghost_1_2'	# Ghost_1_2 == a ghost

    # there are several ghots BUT none at (1,2)
	elif (1,2) not in ghostPos:
		return 'Safe_1_2'	# Safe_1_2 == no ghost

    # anything else
	else:
		return 'Unsafe_1_2'	# Unsafe_1_2 == maybe a ghost

if __name__ == '__main__':
    for tests in someTestStates:
        print is_1_2_safe(state=tests)
        print "\n\n\n"


