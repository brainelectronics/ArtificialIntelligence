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
        for x in range(0, numberOfSets):
            # print "This is #%d" %x

            # mySet = Set()
            # while len(mySet) < numberOfElements:
            #     myRandomNumber = random.randint(min_val, max_val)
            #     if myRandomNumber not in mySet:
            #         mySet.add(myRandomNumber)
            # myList.append(mySet)

            myTuples = ()
            while len(myTuples) < numberOfElements: 
                myRandomNumber = random.randint(min_val, max_val)
                if myRandomNumber not in myTuples:
                    myTuples += (myRandomNumber,)
            myList.append(myTuples)

        return myList

if __name__ == '__main__':
    # print reverse_concatenate([1,24,56], [4,78,894])
    # print list_of_sets(min_val=1, max_val=3, k=4, l=3)
    print list_of_sets(min_val=1, max_val=6, k=3, l=5)