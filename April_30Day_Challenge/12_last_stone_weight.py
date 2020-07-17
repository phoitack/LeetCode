#!/usr/bin/python3

a = [2,7,4,1,8,1]


def lastStoneWeight(stones):

    #for _ in range(len(stones) - 1):
    while len(stones) > 1:

        stones.sort()
        print('*',stones)
        stones.append(stones.pop() - stones.pop())
        print('**',stones)

    return(stones[0])

lastStoneWeight(a)
