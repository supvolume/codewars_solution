""" solution for Closest elevator challenge
return which number is the closet to the call. if equal, return right"""

def elevator(left, right, call):
    if abs(left-call) >= abs(right-call):
        return 'right'
    else:
        return 'left'