""" solution for Find the odd int challenge
find the int that appears an odd number of times"""

def find_it(seq):
    count ={}
    for n in seq:
        count.setdefault(n,0)
        count[n]+=1
    for k,v in count.items():
        if v%2 ==1:
            return k
            break