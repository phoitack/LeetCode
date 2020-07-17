#!/usr/bin/python3


N = 8

def numberOfSteps (num: int) -> int:

    count = 0

    while num > 0:
        if (num%2 == 0):
            num = num / 2
            count += 1
        else:
            num = num - 1
            count += 1

    return(count)


numberOfSteps(N)


'''
class Solution:
    def numberOfSteps (self, num: int) -> int:
        n = 0
        while num != 0:
            odd = num & 1
            num = num >> 1 if not odd else num-1
            n += 1
        return n
'''
