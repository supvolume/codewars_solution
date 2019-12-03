""" solution for the observed PIN challenge
hen given the pin number, it will return the list of possible pin number
which include the possible nearby number of each number in the pin"""

def get_pins(observed):
    zero = ['8','0']
    one = ['1', '2', '4']
    two = ['1', '2', '5', '3']
    three = ['2', '3', '6']
    four = ['1', '4', '5', '7']
    five = ['2', '4', '5', '6', '8']
    six = ['3', '5', '6', '9']
    seven = ['4', '7', '8']
    eight = ['5', '7', '8', '9', '0']
    nine = ['6', '8', '9']
    all_num = [zero, one, two, three, four, five, six, seven, eight, nine]

    possible_list = []
    for i in range(len(observed)):
        possible_list.append(all_num[int(observed[i])])
    if len(possible_list) == 1:
        return possible_list[0]
    else:
        return poss_pin(possible_list)

def poss_pin(poss_list):
    if len(poss_list) == 1:
        return poss_list
    elif len(poss_list) == 2:
        pin_list = []
        for i in range(len(poss_list[0])):
            for j in range(len(poss_list[1])):
                pin = poss_list[0][i]+poss_list[1][j]
                pin_list.append(pin)
        return pin_list
    else:
        return poss_pin(poss_list[:-2] + [poss_pin(poss_list[-2:])])
