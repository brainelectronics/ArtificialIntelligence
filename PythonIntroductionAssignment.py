#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Complete the function named reverse_concatenate. It should take to lists, 
join them into one list and then reverse the order of the result.
"""
def reverse_concatenate(a,b):
    return list(reversed(list(a)+list(b)))

"""
Complete the function below, that should take as input four integers, 
min_val, max_val, k, l. The output should be a list of l sets, each 
containing k integers within the range [min_val,max_val]. Remember that 
because of the nature of the set container, each individual set can only 
contain different numbers. For this reason, you should raise a ValueError 
exception in case it is not possible to construct the desired output structure 
for the given input.

For example, a possible output for a call like 
`list_of_sets(min_val=1,max_val=6,k=3,l=3)` could be:
[{2, 3, 6}, {3, 5, 6}, {3, 4, 6}]
However, `list_of_sets(min_val=1,max_val=3,k=4,l=3)` should raise a `ValueError`.
"""
import random
from sets import Set
def list_of_sets(min_val,max_val,k,l):
    numberOfElements = k
    numberOfSets = l
    myList = []
    # mySet = Set()
    # myTuples = ()
    if (max_val+1-min_val) < numberOfElements:
        # more values wanted, than in range available
        raise ValueError
    else:
        for x in range(numberOfSets):
            # print "This is #%d" %x

            # mySet = Set()
            # while len(mySet) < numberOfElements:
            #     myRandomNumber = random.randint(min_val, max_val)
            #     if myRandomNumber not in mySet:
            #         mySet.add(myRandomNumber)
            # myList.append(mySet)

            #mySet = ()
            mySet = set()
            while len(mySet) < numberOfElements: 
                myRandomNumber = random.randint(min_val, max_val)
                if myRandomNumber not in mySet:
                    # mySet += (myRandomNumber,)
                    mySet.add(myRandomNumber)
            myList.append(mySet)

        return myList


"""
Write a function that returns the formula for the surface area of a 
n-dimensional sphere. The input will be n_dimensions and the output should be 
a function of the symbol r only. Use wikipedia to your advantage.
Make sure you can use the output of the function to compute the actual number 
that is the surface of, say, a 17-dimensional sphere with a radius of 1.338.
"""
"""
import sympy
import math
def sphere_surface_area(n_dimensions):
    # n_dimensions = 17
    r = sympy.symbols('r')
    nenner = 1
    if n_dimensions <= 2:
        # just to be sure, you are not kidding me
        raise ValueError
    if (n_dimensions % 2 == 0): #even 
        '''(2pi^(n/2)*r^(n-1))/2*4*6*....(n-2) if even n'''
        for i in xrange(2, (n_dimensions-2)+1, 2):
            nenner = nenner*i
        formula = ((2*(sympy.pi**(n_dimensions/2))*(r**(n_dimensions-1)))/nenner)
    else: #odd
        '''(2*2pi^((n-1)/2)*r^(n-1))/1*3*5*....(n-2) if odd n'''
        for i in xrange(1, (n_dimensions-2)+1, 2):
            nenner = nenner*i
        formula = ((2*2*(sympy.pi**((n_dimensions-1)/2))*(r**(n_dimensions-1)))/nenner)
        
    return formula
"""

if __name__ == '__main__':
    print reverse_concatenate([1,24,56], [4,78,894])
    print list_of_sets(min_val=1, max_val=3, k=3, l=3)
    print list_of_sets(min_val=1, max_val=6, k=3, l=5)
    # print sphere_surface_area(17)

