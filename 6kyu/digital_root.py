""" solution for Sum of Digits / Digital Root challenge
recursive sum of all the digits in a number untill it become single digit"""

def digital_root(n):
    sepNum = [int(x) for x in str(n)]
    while len(sepNum) != 1:
        sepNum = [int(x) for x in str(n)]
        n = sum(sepNum)
    return n
