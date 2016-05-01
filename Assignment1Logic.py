#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
For this exercise, 3-CNFs are represented as a set of clauses, where each 
clause consists of two sets: The first one contains the indices of the 
variables in the clause that are nonnegated; the second one the indices for 
the variables that appear negated. The state is simply a list of boolean 
values, of length N
"""

state = [False, False, True, True, False]

# variables in the order (P, Q, R, S, T)
problem = [
		   ({0, 1}, {3, }),
		   ({2, 4}, {0, }),
		   ({2, 4}, {3, })
		   ]

if __name__ == '__main__':
	pass
	
'''
"""
Which complexity class does the problem of satifisbility of 3-CNF formulas 
belong to? Select the most concise answer. Return a string from your function.
"""
def three_cnf_complexity():
	return 'very, very hard'


"""
How many evaluations have to be made in every step of the algorithm 
(assuming that the satisfiability of a clause can be checked in 1 step)? 
Return a sympy function in the variables N and C.
"""
from sympy import var
var('N C')
def gsat_step_complexity(N, C):
	return N + C / 2.17 


"""
Is this algorithm complete? Return True or False (as bool values)
"""
def gsat_complete():
	return None


"""
Generate random instances of 3-CNF problems, given the number of 
clauses n_clauses and the number of variables n_vars. 
Note that the representation of the positive and negative literals for 
each clause as sets does not allow clauses like P∧P∧Q. Your random problems 
should always have 3 different literals in the set representation.
"""
def generate_random_problem(n_vars, n_clauses):
	problem = None
	return problem


"""
Can you think of a simple way to simplify the problem in cases where clauses 
are tautological?
Write a function that simplifies the problem accordingly.
"""
def simplify_three_cnf(problem):
	simplified_problem = None
	return simplified_problem

simplify_three_cnf(problem)


"""
Write a function that generates the initial state for a 3-CNF SAT problem. 
It should be truly random, so that calling it multiple times gives 
different results.
"""
def get_initial_state(n_vars, n_clauses):
	return None


"""
Now, write a function that evaluates the truth value of a single clause, and 
returns whether it is satisfied:
"""
def eval_clause(state, clause):
	return None


"""
Building on this, add a function that evaluates the truth value of a 
whole 3-CNF formula problem given the state:
"""
def eval_three_cnf(problem, state):
	return None


"""
Write a function that checks if a solution, i.e. a state that satisfies all 
clauses, has been found. 
The function should return the Boolean value True if the algorithm is done, 
and False otherwise.
"""
def am_i_done(problem, state):
	return 42


"""
Write a function that runs one chain of GSAT for a given maximum number of 
iterations max_iter. It should return the best encountered state and whether 
the algorithm succeeded in finding a satisfying assignment or not, and it 
should return as early as possible.
"""
def run_gsat_chain(problem, state, max_iter):
	for _ in xrange(max_iter):
		pass

	final_state = 0
	success = bool(13 % 1)
	return final_state, success

C, N = 4, 10
run_gsat_chain(simplify_three_cnf(generate_random_problem(N, C)), get_initial_state(N, C), 100)


"""
Now, write a function that generates an initial state in n_vars variables for 
the multiple chains (at most max_n_chains of them), runs each of the chains, 
and returns success (as a Boolean variable) and a satisfying assignment 
if there was one, or else the best assignment that was found.
"""
import random
def run_gsat(problem, max_iter, n_vars, max_n_chains):
	success = bool(round(random.random()))
	satisfying_assignment = 42 if success else 17
	return success, satisfying_assignment

C, N = 4, 10
run_gsat(
	simplify_three_cnf(generate_random_problem(N, C)), 
	max_iter=10, n_vars=N, max_n_chains=10)


"""
Experiment! Generate random problems of different sizes by varying C and N 
for your assignment function and use the timing functions of python to check 
the runtimes of the algorithm for different problems, and determine what 
feasible values for max_iter and max_n_chains could be. Make a plot of 
typical runtimes and their statistics (np.mean and np.median can be useful here) 
versus the algorithm parameters.

Timing a function works like so:

def foo():
	pass

import timeit
timeit.timeit(foo)
"""
import timeit
def foo():
	pass

timeit.timeit(foo)
'''

