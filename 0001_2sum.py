#!/usr/bin/python3

'''
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

nums  = [2,7,1,4,5,11,15,8,1,2,4,5,7]
target = 9

def twoSum(X,y):

    indices = []

    for i in range(len(nums)):
        for j in range(1,len(nums)):

            sum = X[i] + X[j]

            #if sum == target and i not in indices and j not in indices:
            if sum == target and i not in indices and j not in indices:
                temp = [i,j]
                indices.extend(temp)
                #break
            #break

    return(indices)


ind = twoSum(nums,target)

print(ind)

def twoSum1(nums, target):

    indices = []

    for i,num in enumerate(nums):
        delta = target - num
        print(delta)
        #i_delta = nums.index(delta)
        if (delta in nums) and nums.index(delta) != i:
            temp = [i,nums.index(delta)]
            indices.extend(temp)
    return (indices)

ind1 = twoSum1(nums,target)

print(list(ind1))



def twoSum2(nums,target):

    dct = {}

    for i,num in enumerate(nums):
        delta = target - v
        if delta in dct:
            return dct[delta],i

        dct[num] = i
        #print(dct)

ind2 = twoSum2(nums,target)

print(list(ind2))
