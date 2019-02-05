""" solution for Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!! challenge
 find number from a to b that the sum give same number
 eg 89 = 8^1 + 9^2
	  135 = 1^1 + 3^2 + 5^3"""

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    eureka =[]
    for i in range(a,b+1):
        splitNum = list(map(int,str(i)))
        sumDigits = 0
        count = 1
        for j in splitNum:
            sumDigits += j**(count)
            count +=1 
        if sumDigits == i:
            eureka.append(i)
    return eureka
