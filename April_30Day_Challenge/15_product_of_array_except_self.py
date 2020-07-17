#!/usr/bin/python3

a = [1,2,3,4]

from collections import deque


def productExceptSelf(nums):

    out = []

    prod = 1

    for i in range(len(nums)):
        temp = nums
        temp[i] = 1

        prod = 1
        prod = prod*nums[i]

        out.append(prod)

    return(out)

#print(productExceptSelf(a))


def productExceptSelf1(nums):
    prod = []

    product_so_far = 1
    for val in nums:
        prod.append(product_so_far)
        product_so_far = product_so_far*val

    # Now traverse it backward but reset
    product_so_far = 1
    #for i in range(len(nums) - 1, -1, -1):
    for i in reversed(range(len(nums))):
        prod[i] = prod[i]*product_so_far
        product_so_far = product_so_far*nums[i]

    return prod

print(productExceptSelf1(a))



def productExceptSelf2(nums):

    n = len(nums)
    # initialize
    left = [1]*n
    right = [1]*n
    res = [1]*n

    #left[0] = 1
    #right[n-1] = 1

    # Pass through left
    for i in range(1,n):
        left[i] = left[i-1]*nums[i-1]

    # Now reverse
    for j in reversed(range(n-1)):
        right[j] = right[j+1]*nums[j+1]

    # Combine by multiplying left and right
    for k in range(n):
        res[k] = left[k]*right[k]

    return(res)

print(productExceptSelf2(a))
