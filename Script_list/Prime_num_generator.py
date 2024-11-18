#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'primegenerator' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER num
#  2. INTEGER val
#
def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primegenerator(num, val):
    """Generator function to yield prime numbers based on val."""
    primes = []  # To store all prime numbers up to 'num'
    for i in range(2, num + 1):  # Iterate from 2 to num
        if is_prime(i):
            primes.append(i)  # Collect all primes

    if val == 0:  # Yield odd-indexed primes (1-based index)
        for i in range(len(primes)):
            if i % 2 == 1:  # Odd indices in 0-based indexing
                yield primes[i]
    elif val == 1:  # Yield even-indexed primes (1-based index)
        for i in range(len(primes)):
            if i % 2 == 0:  # Even indices in 0-based indexing
                yield primes[i]



if __name__ == '__main__':

    num = int(input().strip())

    val = int(input().strip())

    for i in primegenerator(num, val):
        print(i,end=" ")