""" solution for Next bigger number with the same digits challenge
find the next bigger number that contain the same digit as the original
if no next big number, return -1"""

def ext_bigger(n):
    n = list(str(n))
    len_n = len(n)

    # Looking for the number that bigger than the number on the left
    # from the right. Meaning that from this position to the end should be sorted
    for i in range(len_n-1,0,-1):        
        if n[i-1] < n [i]:
            big_num = n[i-1]

            # create the list from the big num to the end then sort
            next_num_list = n[i-1:]
            next_num_list.sort()

            # find the next big number but not the biggest
            bigger_num = ''
            for j in next_num_list:
                if j > big_num and bigger_num == '':
                    bigger_num = j
                    next_num_list.remove(j) # remove that bigger num from list

            # place the bigger num to the front of the sorted list
            next_num_list.insert(0,bigger_num)

            # combine the non-sorted list (the num in front of big number
            # with the sorted list
            next_bigger_list = n[:i-1]+next_num_list
            
            return int(''.join(next_bigger_list))

    # if not find, return -1
    return -1