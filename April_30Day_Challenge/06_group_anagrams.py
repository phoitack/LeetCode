#!/usr/bin/python3

'''
Given an array of strings, group anagrams together.
'''

A = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(strs):
    my_dict = {}

    for i in range(0,len(strs)):

        key = tuple(sorted(strs[i]))

        if key not in my_dict:

            my_dict[key] = [strs[i]]
        else:
            my_dict[key].append(strs[i])

    return(my_dict.values())

print(groupAnagrams(A))
