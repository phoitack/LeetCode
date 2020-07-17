#!/usr/bin/python3

'''
Defanging an IP address
'''

ip_in = '1.1.1.1'

def defangIPaddr(ip_in):

    ip_out = ip_in.replace('.','[.]')

    return(ip_out)

print(defangIPaddr(ip_in))
