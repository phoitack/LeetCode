#!/usr/bin/python3

'''
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution
using the divide and conquer approach, which is more subtle.
'''

p = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):

    max_curr  = 0
    max_final = 0

    for i in range(0,len(nums)):

        max_final = max_final + nums[i]

        if max_final < 0:
            max_final = 0

        elif max_final > max_curr:
            max_curr = max_final

    return(max_curr)


print(maxSubArray(p))


def maxSubArray1(nums):

    max_curr  = nums[0]
    max_final = nums[0]

    for i in range(1,len(nums)):
        max_curr = max(nums[i],max_curr + nums[i])
        max_final = max(max_curr,max_final)

    return(max_final)


print(maxSubArray1(p))
