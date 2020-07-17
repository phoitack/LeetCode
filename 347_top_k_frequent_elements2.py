'''
Given a non-empty array of integers, return the k most frequent elements.
'''

p = [1,1,1,2,2,3,3,4,5,5,5,5,5]

top = 2

def topKFrequent(nums,k):

    my_dict = {}

    for num in nums:
    	if num in my_dict:
    		my_dict[num] += 1
    	else:
    		my_dict[num] = 1

    lkeys = list(my_dict.keys())
    lval = list(my_dict.values())

    z = []

    for _,j in sorted(zip(lval,lkeys),reverse=True):
    	z.append(j)


    return(z[:k])

print(topKFrequent(p,top))
