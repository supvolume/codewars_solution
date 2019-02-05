""" solution for Remove the minimum challenge
 remove one smallest value from array/list. """
 
def remove_smallest(numbers):
    n = list(numbers)
    if len(n) != 0:
        x = sorted(n)
        n.remove(x[0])
        return n
    else:
        return n
