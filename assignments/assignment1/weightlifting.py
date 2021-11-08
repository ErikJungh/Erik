#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Assignment 1, Problem 1: Weightlifting

Team Number:
Student Names:
'''

'''
Copyright: justin.pearson@it.uu.se and his teaching assistants, 2020.

This file is part of course 1DL231 at Uppsala University, Sweden.

Permission is hereby granted only to the registered students of that
course to use this file, for a homework assignment.

The copyright notice and permission notice above shall be included in
all copies and extensions of this file, and those are not allowed to
appear publicly on the internet, both during a course instance and
forever after.
'''
from re import sub
import re
from typing import *  # noqa
import unittest  # noqa
import math  # noqa
from src.weightlifting_data import data  # noqa
# If your solution needs a queue, then you can use this one:
from collections import deque  # noqa
# If you need to log information during tests, execution, or both,
# then you can use this library:
# Basic example:
#   logger = logging.getLogger("put name here")
#   a = 5
#   logger.debug(f"a = {a}")
import logging  # noqa

__all__ = ['weightlifting', 'weightlifting_subset']
# Sort set in n*log(n) time as justin requested.
def mergeSort(set):
   
    if len(set) > 1:
        mid = len(set) // 2
        left = set[:mid]
        right = set[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              set[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                set[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            set[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            set[k]=right[j]
            j += 1
            k += 1

def find_subset(A, depth, weight, lookup):
 
    # return true if the sum becomes 0 (subset found)
    if weight == 0:
        return True
 
    # base case: no items left, or sum becomes negative
    if depth < 0 or weight < 0:
        return False
 
    # construct a unique key from dynamic elements of the input
    key = (depth, weight)
 
    # if the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:
 
        # Case 1. Include the current item `A[depth]` in the subset and recur
        # for the remaining items `depth-1` with the decreased total `weitgh-A[DEPTH]`
        include = find_subset(A, depth - 1, weight - A[depth], lookup)
 
        # Case 2. Exclude the current item `A[depth]` from the subset and recur for
        # the remaining items `depth-1`
        exclude = find_subset(A, depth - 1, weight, lookup)
 
        # assign true if we get subset by including or excluding the current item
        lookup[key] = include or exclude
        
    # return solution to the current subproblem
    
    return lookup[key]


def subset(array, num):
    print("finding weight: " + str(num))
    if(num == 0):
        return set()
    result = []
    def find(arr, num, path=()):
        if not arr or arr[0] > num:
            return
        if arr[0] == num:
            result.append(path + (arr[0],))
        else:
            find(arr[1:], num - arr[0], path + (arr[0],))
            find(arr[1:], num, path)
    find(array, num)
    
    if len(result)>0:
        
        return set(result[0])
        
    else:
        print(set())
        return set()
    #return result
 
 
def weightlifting(P: Set[int], weight: int) -> bool:
    '''
    Sig:  Set[int], int -> bool
    Pre:
    Post:
    Ex:   P = {2, 32, 234, 35, 12332, 1, 7, 56}
          weightlifting(P, 299) = True
          weightlifting(P, 11) = False
    '''
    plate_list = list(P)
    # Initialise the dynamic programming matrix
    dp_matrix = [
        [None for i in range(weight + 1)] for j in range(len(plate_list) + 1)
    ]
    
    mergeSort(plate_list)
    
    depth = len(plate_list)
    #print('trying to find weight: ' + str(weight) + ' in subset w')
    return find_subset(plate_list, depth-1, weight, {})




def weightlifting_subset(P: Set[int], weight: int) -> Set[int]:
    '''
    Sig:  Set[int], int -> Set[int]
    Pre:
    Post:
    Ex:   P = {2, 32, 234, 35, 12332, 1, 7, 56}
          weightlifting_subset(P, 299) = {56, 7, 234, 2}
          weightlifting_subset(P, 11) = {}
    '''
    
    
    plate_list = list(P)
    mergeSort(plate_list)
    depth = len(plate_list)
    #print('trying to find weight: ' + str(weight) + ' in subset s')
   
    return_set = subset(plate_list, weight)
    print("value becomes " + str(return_set))
    return set(return_set)
        
    
    


class WeightliftingTest(unittest.TestCase):
    """
    Test Suite for weightlifting problem

    Any method named "test_something" will be run when this file is executed.
    Use the sanity check as a template for adding your own test cases if you
    wish. (You may delete this class from your submitted solution.)
    """
    logger = logging.getLogger('WeightLiftingTest')
    data = data
    weightlifting = weightlifting
    weightlifting_subset = weightlifting_subset

    def test_satisfy_sanity(self):
        """
        Sanity Test for weightlifting()

        passing is not a guarantee of correctness.
        """
        plates = {2, 32, 234, 35, 12332, 1, 7, 56}
        self.assertTrue(
            WeightliftingTest.weightlifting(plates, 299)
        )
        self.assertFalse(
            WeightliftingTest.weightlifting(plates, 11)
        )

    def test_subset_sanity(self):
        """
        Sanity Test for weightlifting_subset()

        passing is not a guarantee of correctness.
        """
        plates = {2, 32, 234, 35, 12332, 1, 7, 56}
        weight = 299
        sub = WeightliftingTest.weightlifting_subset(plates, weight)
        for p in sub:
            
            self.assertIn(p, plates)
            
        self.assertEqual(sum(sub), weight)

        weight = 11
        sub = WeightliftingTest.weightlifting_subset(plates, weight)
        self.assertSetEqual(sub, set())

    def test_satisfy(self):
        for instance in self.data:
            self.assertEqual(
                WeightliftingTest.weightlifting(instance["plates"], instance["weight"]), instance["expected"]
            )

    def test_subset(self):
        """
        Sanity Test for weightlifting_subset()

        passing is not a guarantee of correctness.
        """
        for instance in self.data:
            plates = WeightliftingTest.weightlifting_subset(
                instance["plates"].copy(),
                instance["weight"]
            )
            self.assertEqual(type(plates), set)

            for plate in plates:
                self.assertIn(plate, instance["plates"])

            if instance["expected"]:
                self.assertEqual(
                    sum(plates),
                    instance["weight"]
                )
            else:
                self.assertSetEqual(
                    plates,
                    set()
                )


if __name__ == '__main__':
    # Set logging config to show debug messages.
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
