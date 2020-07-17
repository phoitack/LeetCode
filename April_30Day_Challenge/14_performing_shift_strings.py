#!/usr/bin/python3

'''
You are given a string s containing lowercase English letters, and a matrix shift,
where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift).
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to
the beginning. Return the final string after all operations.

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation:
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
'''

from collections import deque

ss = 'abc'
ops = [[0,1],[1,2]]

#ss = 'abcdefg'
#ops = [[1,1],[1,1],[0,2],[1,3]]

#ss = 'mecsk'
#ops = [[1,4],[0,5],[0,4],[1,1],[1,5]]

def stringShift(s,shift):

    c = 0
    lr = 0

    for elem in shift:
        #c = c + 2*elem[0] - 1

        if elem[0] > 0:
            lr  = lr + elem[1]
        else:
            lr  = lr - elem[1]

        #print('c =',c)
        #print('lr =',lr,'\n')

    sd = deque(s)

    #for k,v in my_dict.items():
    #sn = []
    sd.rotate(lr)

    return(''.join(list(sd)))



print(stringShift(ss,ops))

'''
def stringShift1(s,shift):

    sd = deque(s)

    for elem in shift:

        if elem[0]

        print('c =',c)
        print('lr =',lr,'\n')

    shiftd = deque(s)

    #for k,v in my_dict.items():
    #sn = []
    shiftd.rotate(lr)

    return(''.join(list(shiftd)))
'''
