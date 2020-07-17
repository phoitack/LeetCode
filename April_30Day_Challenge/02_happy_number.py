#!/usr/bin/python3

num = 7

def isHappy(n):
    '''
    a = list(map(int,str(n)))

    total = sum(map(lambda x: x*x,a))

    while total != 1 or len(total) > 1:
        #print('HeLLO')
        a = list(map(int,str(total)))
        total = sum(map(lambda x: x*x,a))
    '''

    visited = set()

    while n!=1 and not n in visited:
        visited.add(n)
        n = sum(map(lambda x:int(x)**2, str(n)))

    return (not n in visited)


print(isHappy(num))
