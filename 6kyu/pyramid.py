""" solution for Pyramid Array challenge"""

def pyramid(n):
    floor = []
    for i in range(n):
        floor.append([1]*(i+1))
    return floor