""" solution for Find The Parity Outlier challenge"""

def find_outlier(integers):
    even = []
    odd = []
    for number in integers:
        if number%2 == 0:
            even.append(number)
        else:
            odd.append(number)
    if len(even) == 1:
        return(even[0])