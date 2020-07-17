#!/usr/bin/python3

'''
Given two strings S and T, return if they are equal when both are typed
into empty text editors. # means a backspace character.
'''

import re

s1 = 'ab#c'
t1 = 'ad#c'

s2 = 'ab##'
t2 = 'c#d#'

s3 = 'a##c'
t3 = '#a#c'

s4 = 'a#c'
t4 = 'b'

pattern1 = '*#'

def _helper(s):
    stack = []

    #count = 0

    for w in s:
        if w != '#':
            #count += 1
            #print(count,'FIRST')
            stack.append(w)
            #print(stack)
        elif stack:  # You need this because there is a danger that stack is empty
            #count += 1
            #print(count,'SECOND')
            stack.pop()
            #print(stack)

    return stack

def backspaceCompare(S,T):

    S = _helper(S)
    T = _helper(T)

    #while pound in S or T:
        #print(S,T)
    #for w in S and T:
    #    print(S,T)

    return (S==T)

print(backspaceCompare(s3,t3))



#print(_helper(s2))
