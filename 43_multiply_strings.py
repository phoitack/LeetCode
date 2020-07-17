#!/usr/bin/python3

'''
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Cannot use int()
'''

def convert_to_int(n:str) -> int:

    result = 0

    my_num = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}

    for i in n:
        result = 10*result + my_num[i]

    return(result)

def multiply(num1:str,num2:str) -> str:

    num1_int = convert_to_int(num1)
    num2_int = convert_to_int(num2)

    total = num1_int*num2_int

    return(str(total))

x = "2"
y = "3"

print(multiply(x,y))




#print(convert_to_int(x))
