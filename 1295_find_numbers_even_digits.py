#!/usr/bin/python3

A = [12,345,2,6,7896]

def findNumbers(nums):

    count = 0

    for num in nums:
        s_num = str(num)
        if len(s_num)%2 == 0:
            count += 1

    return(count)
        #print(s_num.split())

print(findNumbers(A))
