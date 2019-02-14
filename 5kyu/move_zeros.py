""" solution for Moving Zeros To The End challenge
move zero to the end of the array"""

def move_zeros(array):
    no_zero = []
    zero = []
    for a in array:
        if a == "0":
            no_zero.append(a)
        elif (str(a) == "0.0" or str(a) == "0" or a == 0) and str(a) != "False":
            zero.append(a)
        else:
            no_zero.append(a)
    return no_zero+zero