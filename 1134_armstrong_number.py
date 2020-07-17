#!/usr/bin/python3

'''
The k-digit number N is an Armstrong number if and only if the k-th power
of each digit sums to N.

Given a positive integer N, return true if and only if it is an
Armstrong number.
'''

n = 123

def isArmstrong(N):

    k = len(str(N))

    num = sum(map(lambda x: int(x)**k,str(N)))

    #if num==N:
    return(num==N)
    #else:
        #return(False)


print(isArmstrong(n))
