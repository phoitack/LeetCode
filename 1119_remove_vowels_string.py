#!/usr/bin/python3

#from orderedset import OrderedSet

'''
Script to remove vowels from a starting
'''

string = "leetcodeisacommunityforcoders"
lstring = list(string)

#print(lstring)

#set_string = set()
vowels = ['a','e','i','o','u']

#print(OrderedSet(string))

for elem in string:
    if elem in vowels:
        lstring.remove(elem)

new = ''.join(lstring)

print(new)

#print(lstring)

'''
def removeVowels(self, S: str) -> str:
S = S.replace('e','')
S = S.replace('a','')
S = S.replace('i','')
S = S.replace('o','')
S = S.replace('u','')
return S
'''
