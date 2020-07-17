#!/usr/bin/python3

p = [1,3,2,3,5,0] # 3
p = [1,1,2,2]  # 2
#p = [1,1,3,3,5,5,7,7]  # 0

def countElesments(arr):

    arr_s = set(arr)
    arr_s = sorted(list(arr_s))

    #delta = []

    count = 0

    for i in range(0,len(arr_s)-1):

        dtemp = arr_s[i+1] - arr_s[i]

        if dtemp == 1 or dtemp == 0:
            count += 1

    return(count)

#print(countElesments(p))


def countElesments1(arr):

    from collections import Counter

    arr = sorted(arr)

    my_dict = Counter(arr)

    #for i in range(0,len(arr)):
    #    my_dict[arr[i]] = arr.count(arr[i])

    lkeys = list(my_dict.keys())
    lvalues = list(my_dict.values())

    sum = 0

    for k in range(0,len(lkeys)-1):
        d = lkeys[k+1] - lkeys[k]
        if d == 1:
            sum += lvalues[k]

    #print(lkeys,lvalues)

    #for k in range(0,len(my_dict)-1):

    #    print(my_dict.key(k))

    return(sum)

print(countElesments1(p))
