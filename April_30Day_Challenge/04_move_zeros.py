#!/usr/bin/python3

# 283 move zeroes

A = [0,1,0,3,12]

def moveZeroes(nums):

    output = []

    count = 0

    n = len(nums)

    for num in nums:
        if num != 0:
            output.append(num)
            count += 1

    zeros = [0]*(n - count)

    output.extend(zeros)

    return(output)


#print(moveZeroes(A))


'''
j = 0
        for i in range(1, len(nums)):
            if nums[j] != 0:
                j += 1
            if nums[i] != 0 and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
'''


def moveZeroes1(nums):
    
    i = j = 0

    while j < len(nums):
        if nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]

        # wait while we find a non-zero element to
        # switch with you
        if nums[i] != 0:
            i += 1

        # keep going
        j += 1

        print(nums,i,j)

moveZeroes1(A)
