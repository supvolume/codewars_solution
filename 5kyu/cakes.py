""" solution for Pete, the baker challenge
 find how make cake that can be make from recipe and available ingredients"""

def cakes(recipe, available):
    numCake = []
    for k,v in recipe.items():
        if (k in available.keys()) == False:
            return 0
            break
        else:
            numCake.append(int(available[k]/v))
    return min(numCake)
