
'''
Given a non-empty array of integers, return the k most frequent elements.
'''

p = [1,1,1,2,2,3,3,4,5,5,5,5,5]
top = 2

from collections import Counter


def topKFrequent(nums,k):

    my_dict = {}

    my_dict = Counter(nums)

    lkeys = list(my_dict.keys())
    lvalues = list(my_dict.values())

    z = []

    # Use zip
    for _,j in sorted(zip(lvalues,lkeys),reverse=True):
        z.append(j)


    #print(lkeys)

    return(z[:k])

print(topKFrequent(p,top))
