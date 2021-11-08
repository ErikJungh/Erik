#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List
'''
Copyright: justin.pearson@it.uu.se and his teaching assistants, 2020.

This file is part of course 1DL231 at Uppsala University, Sweden.
'''
__all__ = ['insertion_sort']

def insertion_sort(A: List[int]):
    """
    Sig:  List[int] ->
    Pre:  (none)
    Post: A is a non-decreasingly ordered permutation of its original elements
    Ex:   A = [5, 7, 3, 12, 1, 7, 2, 8, 13]
          insertion_sort(A)
          # A is now [1, 2, 3, 5, 7, 7, 8, 12, 13]
    """
    for j in range(1, len(A)):
        # Invariant: A[0..j-1] is a sorted permutation of its original elements
        # Variant: len(A) - j
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:  #* \label{line:ins-sort-while}
            # Invariant: A[i+2..j] has the original elements of A[i+1..j-1]
            # Variant: i
            A[i+1] = A[i]
            i = i - 1  #* \label{line:ins-sort-while-end}
        A[i + 1] = key


def main():
    """
    Test case.

    Will run if this file is executed from the command line.
    """
    A = [5, 7, 3, 12, 1, 7, 2, 8, 13]
    insertion_sort(A)
    print(A)
    if A == [1, 2, 3, 5, 7, 7, 8, 12, 13]:
        print('Test succeeded!')
    else:
        print("[1, 2, 3, 5, 7, 7, 8, 12, 13] expected --- test failed!")


if __name__ == '__main__':
    main()
