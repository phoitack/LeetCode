#!/usr/bin/python3

a = [0,1,0]

def findMaxLength(nums):

    n = len(nums)

    count = 0

    if n > 2:
        for i in range(n-1):
            delta = abs(nums[i+1] - nums[i])
            if delta == 1:
                count += 1
        return(count)
    elif n == 1:
        return(0)
    else:
        delta = abs(nums[1]-nums[0])
        if delta == 0:
            return(0)
        else:
            return(2)


print(findMaxLength(a))


def findMaxLength1(self, nums: List[int]) -> int:

    partial_sum = 0

	# table is a dictionary
	# key : partial sum value
	# value : the left-most index who has the partial sum value

    table = { 0: -1}

    max_length = 0

    for idx, number in enumerate( nums ):

        # partial_sum add 1 for 1
        # partial_sum minus 1 for 0

        if number:
            partial_sum += 1
        else:
            partial_sum -= 1


        if partial_sum in table:

            # we have a subarray with equal number of 0 and 1
            # update max length

            max_length = max( max_length, ( idx - table[partial_sum] ) )

        else:
            # update the left-most index for specified partial sum value
            table[ partial_sum ] = idx

    return max_length


def findMaxLength2(self, nums: List[int]) -> int:

    c,d,m = 0,{0:0},0    # Dictionary, key = counts, value is the index

    for i,v in enumerate(nums):
        c += 2*v - 1  # +1 if v ==1 or -1 if v==0
        if c in d:    # have we seen that count of 0/1s before?
            m = max(m,i+1-d[c])  # was that subarray longer?
        else:
            d[c] = i+1            # no, this is the first time, let's add that index for that c
    return m



def findMaxLength2(self, nums: List[int]) -> int:

    c,d,m = 0,{0:-1},0    # Dictionary, key = counts, value is the index

    for i,v in enumerate(nums):
        c += 2*v - 1  # +1 if v ==1 or -1 if v==0
        if c in d:    # have we seen that count of 0/1s before?
            m = max(m,i-d[c])  # was that subarray longer?
        else:
            d[c] = i            # no, this is the first time, let's add that index for that c
    return m
