#!/usr/bin/python3

'''
Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid. We define the validity
of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left
parenthesis '(' or an empty string.

An empty string is also valid.
Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True
'''


def checkValidString(s):
    left_stack, star_stack = list(), list()
    for index, letter in enumerate(s):
        if letter == "(":
            left_stack.append(index)
        elif letter == "*":
            star_stack.append(index)
        else:
            """
            if extra '(' is in there, pop it off
            """
            if left_stack:
                left_stack.pop()
            elif star_stack: # if no extra '(' is present, use '*' as '(', match and pop off
                star_stack.pop()
            else:
                return False

    if not left_stack:
        """
        if no open '(' is present, all '*' are left as open blanks, hence return true
        """
        return True
    else:
        """we have to check otherwise, if * can be used to close an open bracket or not.
        ie, if star is present before open bracket, then its of no use to close, we will use it
        as a space, only if it is present after the index of first element in left_stack, it can be
        converted as a closing bracket and can be used.
        """

        first_elem = left_stack[0]
        while star_stack:
            if star_stack[0] < first_elem:
                star_stack.pop(0)
            else:
                star_stack.pop(0)
                left_stack.pop(0)
                if left_stack:
                    first_elem = left_stack[0]
                else:
                    return True
        return False



ss = '(*))'


print(checkValidString(ss))
