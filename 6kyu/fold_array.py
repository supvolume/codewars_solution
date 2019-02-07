""" solution for Fold an array challenge
 sum the number of head with tail and sum the next number from head with previous number of tail
 then if have middle number, append to the new array
 repeat for runs times"""

def fold_array(array, runs):
    for r in range(runs):
        half = int(len(array)/2)
        middle = array[half]
        hasMiddle = (len(array)%2 ==1)
        array = [sum(x) for x in zip(array[:half],list(reversed(array[-half:])))]
        if hasMiddle ==True:
            array.append(middle)
    return array