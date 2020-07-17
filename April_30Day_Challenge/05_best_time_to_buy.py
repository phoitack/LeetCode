#!/usr/bin/python3

'''
Say you have an array for which the ith element is the price of a given
stock on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).
'''

#p = [1,2,3,4,5]
p = [7,6,4,3,1]
p = [7,1,5,3,6,4]

def maxProfit(prices):

    sum = 0

    for i in range(0,len(prices)-1):

        if prices[i+1] > prices[i]:
            # buy
            delta = prices[i+1] - prices[i]
            sum = sum + delta

    return(sum)

print(maxProfit(p))


def maxProfit1(prices):

    sum = 0

    for i in range(0,len(prices)-1):

        delta = prices[i+1] - prices[i]

        sum = sum + max(delta,0)

    return(sum)

print(maxProfit(p))
