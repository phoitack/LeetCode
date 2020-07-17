#!/usr/bin/python3

'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

'''

a = [2,2,2,2,2,1]

from collections import Counter

def singleNumber(nums):

    A = Counter(nums)

    for k in A:
        if A[k]==1:
            return(k)

        #print(k,A[k])

print(singleNumber(a))


def singleNumber1(nums):

    my_dict = {}

    for k in range(0,len(nums)):
        my_dict[nums[k]] = nums.count(nums[k])

    for k in my_dict:
        if my_dict[k]==1:
            return(k)

    #print(my_dict)

    #return(my_dict.value(1))

print(singleNumber1(a))
