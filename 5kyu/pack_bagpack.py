""" solution for Packing your backpack challenge
find maximum score to fit in bagpack with given capacity"""

# NOT FINISH

def pack_bagpack(scores, weights, capacity):
    bagpack_list = list(zip(scores, weights))
    bagpack_list.sort(reverse = True)
    max_score = 0
    total_cap = 0
    for i in range(len(bagpack_list)):
        if bagpack_list[i][1] + total_cap <= capacity:
            max_score += bagpack_list[i][0]
            total_cap += bagpack_list[i][1]
    return max_score