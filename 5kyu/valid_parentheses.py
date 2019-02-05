""" solution for Valid Parentheses challenge
 find the valid order and number of parentheses"""

def valid_parentheses(string):
    count = 0
    for x in list(string):
        if count < 0:
            break
        elif x == '(':
            count += 1
        elif x == ')':
            count -= 1
    if count == 0:
        return True
    else:
        return False
