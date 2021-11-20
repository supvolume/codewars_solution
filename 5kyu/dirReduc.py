""" solution for Directions Reduction challenge
remove the path that are opposite """

def dirReduc(arr):
    prv_n = 0
    n = len(arr)
    new_arr = []
    while prv_n != n:
        for i in range(len(arr)-1):
            if (arr[i] == "NORTH" and arr[i+1] == "SOUTH") or \
               (arr[i] == "SOUTH" and arr[i+1] == "NORTH") or \
               (arr[i] == "EAST" and arr[i+1] == "WEST") or \
               (arr[i] == "WEST" and arr[i+1] == "EAST"):
                del arr[i:i+2]
                break
        prv_n = n
        n = len(arr)
    return arr


#Test
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
