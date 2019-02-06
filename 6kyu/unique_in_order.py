"""solution for Unique In Order challenge
reduce repeating items that are next to each other and return items in the same order"""

def unique_in_order(iterable):
    ordered = []
    sepItems = list(iterable)
    previous_x =''
    for x in sepItems:
        if x != previous_x:
            ordered.append(x)
        previous_x = x
    return ordered
