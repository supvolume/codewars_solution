""" solution for T.T.T.17: Split odd and even challenge
split odd and even number from a given n number"""

def split_odd_and_even(n):
    str_n = str(n)
    split_numbers = []
    split_n = str_n[0]
    for i in range(1,len(str_n)):
        if int(split_n)%2 == int(str_n[i])%2:
            split_n = split_n + str_n[i]
        else:
            split_numbers.append(int(split_n))
            split_n = str_n[i]
    split_numbers.append(int(split_n))
    return split_numbers