'''
Given an array of numbers nums, in which exactly two elements appear 
only once and all the other elements appear 
exactly twice. Find the two elements that appear only once.
'''

def singleNumber(nums):

    from collections import Counter

    s = Counter(nums)

    my_list = []

    for key, value in s.items():
        if value == 1:
            my_list.append(key)


    return (my_list)
    
A = [1, 2, 1, 3, 2, 5]

print(singleNumber(A))