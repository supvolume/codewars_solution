""" solution for Sum of Intervals challenge
find the intervals length from the given list of array
https://www.codewars.com/kata/52b7ed099cdc285c300001cd/python"""


# Merge the list that has duplicate intervals
def merge_int(expand_ints):
    int_len = 0
    first = 0
    second = 0
    while first < len(expand_ints):
        int_len = len(expand_ints)
        if second >= len(expand_ints):
            first += 1
            second = 0
        elif first >= len(expand_ints):
            break
        else:
            if first != second:
                for each_int in expand_ints[first]:
                    if each_int in expand_ints[second]:
                        expand_ints[first] = list(set(expand_ints[first]+expand_ints[second]))
                        expand_ints.remove(expand_ints[second])
                        break
            second += 1
    return expand_ints

def sum_of_intervals(intervals):
    # Expand intervals from array of start and end to full list
    expand_ints = []
    for i in intervals:
        expand_int = []
        for each_num in range(i[0], i[-1]+1):
            expand_int.append(each_num)
        expand_ints.append(expand_int)

    # Loop until the length does not change
    for i in expand_ints:
        expand_ints = merge_int(expand_ints)

    # Sum intervals
    count = 0
    for i in expand_ints:
        i.sort()
        count += i[-1]-i[0]
    
    return count


# Test
#print(sum_of_intervals([(1, 5)])) #4
#print(sum_of_intervals([(1, 5), (6, 10)])) #8
#print(sum_of_intervals([(1, 5), (1, 5)])) #4
#print(sum_of_intervals([(1, 4), (7, 10), (3, 5)])) #7
#print(sum_of_intervals([[1,5],[10, 20],[1, 6],[16, 19],[5, 11]])) #19
print(sum_of_intervals([(-488, -187), (235, 423), (283, 433), (-6, 487),
                        (358, 469), (263, 286), (353, 408), (184, 429),
                        (377, 483), (-37, 227), (56, 219), (422, 450),
                        (-41, 305)])) # 829
