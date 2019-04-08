""" solution forIQ Test challenge
find the order (index+1) of different number (odd and even) from a list of number
use Python 2.7.6"""

def iq_test(numbers):
    number_list = map(int, numbers.split())
    odd = []
    even = []
    for n in number_list:
        if n%2 == 1:
            odd.append(n)
        else:
            even.append(n)
    if len(odd) == 1:
        return number_list.index(odd[0])+1
    else:
        return number_list.index(even[0])+1