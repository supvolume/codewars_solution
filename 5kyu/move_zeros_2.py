""" solution for Moving Zeros To The End challenge"""

def move_zeros(array):
    return_list = []
    zero_list = []
    for i in array:
        if i == 0 and (type(i) == int or type(i) == float):
            zero_list.append(i)
        else:
            return_list.append(i)
    return return_list+zero_list


# test
print(move_zeros([0,1,None,2,False,1,0]))
