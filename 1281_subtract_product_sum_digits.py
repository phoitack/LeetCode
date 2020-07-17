#!/usr/bin/python3

import numpy as np

num = 234

def subtractProductAndSum(n):

    ns = list(map(int,str(n)))

    sum = 0
    prod = 1

    while n > 0:
        print('1:',n)
        sum = sum + n%10
        prod = prod*(n%10)

        n = n / 10
        n = int(n)

        print('2:',n,'\n')

    #sum = np.sum(ns)
    #prod = np.prod(ns)

    result = prod - sum

    print(result)

    return(result)

subtractProductAndSum(num)
