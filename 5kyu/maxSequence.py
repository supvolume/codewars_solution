""" solution for Maximum subarray sum challenge
find the maximum sum of contiguous subsequence in an array
and return the maximum sum"""

def maxSequence(arr):
    non_neg_index_list = []
    max_sum_list = []

    # find index of non negative number
    for i in range(len(arr)):
        if arr[i] >= 0:
            non_neg_index_list.append(i)

    # return 0 if only negative number presented in the arr
    if len(non_neg_index_list) == 0:
        return 0

    # create a possible list from non_neg_index_list and find sum
    else:
        for i in non_neg_index_list:
            for j in list(reversed(non_neg_index_list)):
                if j > i and sum(arr[i:j+1]) > sum(max_sum_list):
                        max_sum_list = arr[i:j+1]
    
    return sum(max_sum_list)


# test
def main():
    sample = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSequence(sample))

if __name__ == "__main__":
    main()
