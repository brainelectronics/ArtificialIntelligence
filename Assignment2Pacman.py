#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
In this exercise you are going to implement part of a propositional system for 
a Pacman Agent. Given the limitations of propositional logic, it is going to be 
a very simple system, but it should serve to illustrate the concept.
The point of this exercise is to use propositional logic lo localize the ghost 
in a 4x4 map. This is made difficult by the fact that Pacman can not see further
than one step in the grid, so he does not have access to the full state, but his
perception only consists of a chill when he is in a square adjacent to a ghost.
"""
"""
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

[['0', '.', '.', '0'],
 ['.', 'C', 'G', 'C'],
 ['0', '.', 'C', '0'],
 ['0', '.', '.', '0']]

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
import pprint
def show_state(state, ghost_pos=None):
    """Show the state graphically, and the position of the ghost, if it is known"""
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
# done?


def is_1_2_safe(state):
    """a function that determines in a propositional way if it safe to move to the (1, 2) square."""
    """
    Safe_1_2 == no ghost
    Unsafe_1_2 == maybe a ghost
    Ghost_1_2 == a ghost
    """
    chillyNeighbourhood = ['C_1_1', 'C_1_3', 'C_2_2', 'C_0_2']
    saveNeighbourhood = ['-C_1_1', '-C_1_3', '-C_2_2', '-C_0_2']
    unknownNeighbourhood = ['NV_1_1', 'NV_1_3', 'NV_2_2', 'NV_0_2']
    chillyNeighbours = set(state).intersection(chillyNeighbourhood)
    saveNeighbours = set(state).intersection(saveNeighbourhood)
    unknownNeighbours = set(state).intersection(unknownNeighbourhood)
    
    #if len(saveNeighbours)>=3:
    #    return 'Safe_1_2'
        # garantiert wahr
        
    if (len(chillyNeighbours) == 2) and len(saveNeighbours) >= 1:
        return 'Safe_1_2'
    elif (len(chillyNeighbours) >= 3):
    #elif (('C_2_2' and 'C_0_2') in state) or (('C_1_1' and 'C_1_3') in state):
        return 'Ghost_1_2'
    else:
        return 'Unsafe_1_2'

