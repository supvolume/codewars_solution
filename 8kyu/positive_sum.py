""" solution for Sum of positive challenge
 sum positive number only"""

def positive_sum(arr):
    posSum = 0
    for i in arr:
        if i > 0:
            posSum +=i
    return posSum
