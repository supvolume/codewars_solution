""" solution for Upside-Down Pyramid Addition...REVERSED! challenge
given the right side of the pyramid, find the top level (original) of the pyramid"""

def reverse(right):
    pyramid = [right[-1]]
    top_floor = right
    bottom_floor = []
    for _ in range(len(right)-1):
        for i in range(len(top_floor)-1):
            room = top_floor[i]-top_floor[i+1]
            bottom_floor.append(room)
        pyramid.append(bottom_floor[-1])       
        top_floor = bottom_floor
    pyramid.reverse()
    return pyramid