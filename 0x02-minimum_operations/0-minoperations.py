#!/usr/bin/python3
def minOperations(n):
    """return minimum number of operations needed"""
    if (n == 1):
        return 0
    count = 0
    i = 2
    while n > 1:
        while n % i == 0:
            count = count + i
            n = n/i
        i = i+1
    return count
  
