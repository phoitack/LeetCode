#!/usr/bin/python3

A = [0,1,2,3,4]

ind = [0,1,2,2,1]

# Use insert(index,element)

def createTargetArray(nums,index):

    new = []

    for i in range(0,len(index)):
        new.insert(index[i],nums[i])

    return(new)


print(createTargetArray(A,ind))
