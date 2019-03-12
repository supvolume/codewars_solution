""" solution for Persistent Bugger challenge
count how many times the number get multiply untill it reach a single digit"""

def persistence(n) :
    count = 0
    numList = list(str(n))
    while len(numList) !=1:
        n = 1
        for i in numList:
            n *= int(i)
        numList = list(str(n))
        count += 1
    return count    