""" solution for All Star Code Challenge #19 challenge
create slogan from given words. The given words might be duplicate but the final slogan can't have duplicated words.
The order of the slogans has to be the same with the order of the original array"""

import itertools

def slogan_maker(array):
    # remove duplicate without reorder
    new_array = []
    for word in array:
        if word not in new_array:
            new_array.append(word)
    # create slogan
    slogans = []
    slo_list = list(itertools.permutations(new_array))
    for slogan in slo_list:
        slogans.append(' '.join(slogan))
    return slogans