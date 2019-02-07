""" solution for Snail Sort challenge
 spread n*n clockwise snailshell pattern to list"""

def snail(array):
    sizeList = list(range(len(array)+1))
    n = len(array)
    m = 0 #length of distance from edge
    repeat = n*2-1 #number of line in snail, which equal to repeat time
    spread = []
    count = 1
    if array ==[[]]:
            spread = []
    else:
        for t in range(repeat):
            if count == 1:    #top of the snail
                for i in range(n-m):
                    spread.append(array[m][i+m])
                count+=1
            elif count == 2:    #right of the snail
                for i in range(n-m-1):
                    spread.append(array[i+m+1][n-1])
                count+=1
            elif count == 3:    #bottom of the snail
                for i in list(reversed(range(n-m-1))):
                    spread.append(array[n-1][i+m])
                count+=1
            elif count == 4:    #left of the snail
                for i in list(reversed(range(n-m-2))):
                    spread.append(array[i+m+1][m])
                count = 1
                m+=1 #move inside of the snail
                n-=1
    return spread