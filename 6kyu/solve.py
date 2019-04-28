""" solution for Upside down numbers challenge
find the number in range that still remain the same if rotate 180 degrees"""

def solve(a,b):
    rotatable = ['0','1','6','8','9']
    same_rotate = ['0','1','8']
    count = 0
    for i in range(a,b):
        each_num = list(str(i))
        while True:
            if len(each_num) == 0:  # multiple digit that has even digit
                count += 1
                break
            elif len(each_num) == 1:
                if str(i)[int(len(str(i))/2)] in same_rotate:  # single digit or middle number from multiple digit
                    count += 1
                    break
                else:
                    break
            else:
                front = each_num.pop(0)
                back = each_num.pop(-1)
                if (front == '0' and back == '0') or (front == '1' and back == '1') or (front == '6' and back == '9') or (front == '8' and back == '8') or (front == '9' and back == '6'):
                    continue
                else:
                    break
    return count