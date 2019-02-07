""" solution for Snail Sort challenge
 spread n*n clockwise snailshell pattern to list"""

        
def snail(array):
	sizeList = list(range(len(array)+1))
	n = len(array)
	repeat = n*2-1 #number of line in snail, which equal to repeat time
	spread = []
	count = 1
	m = 0
	if array ==[[]]:
		spread = [[]]
	else:
		for t in range(repeat):
			if count == 1:
				for i in range(n-m):
					spread.append(array[m][i+m])
				count+=1
			elif count == 2:
				for i in range(n-1-m):
					spread.append(array[i+1+m][n-1])
				count+=1
			elif count == 3:
				for i in list(reversed(range(n-1-m))):
					spread.append(array[n-1][i+m])
				count+=1
			elif count == 4:
				for i in list(reversed(range(n-2-m))):
					spread.append(array[i+1+m][m])
				count = 1
				m+=1
				n-=1
	print(spread)
