""" solution for Count the Digit challenge challenge"""

def nb_dig(n,d):
    count = 0
    for i in range(0,n+1):
        square = i*i
        for j in str(square):
            if j == str(d):
                count += 1
    return count