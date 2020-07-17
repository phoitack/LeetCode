#!/Users/phoitack/anaconda3/bin/python

import tensorflow as tf

def search(nums,target):

    L = 0
    R = len(nums) - 1

    while L <= R:
        mid = (L + R)//2

        if nums[mid] == target:
            return(mid)
        elif nums[mid] < target:
            L = mid + 1
        else:
            R = mid - 1
        print(mid,L,R)

    #print('hello')

    return(-1)

ss = [4,5,6,7,0,1,2]

print(search(ss,0))
