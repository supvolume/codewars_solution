"""solution for Down Arrow With Numbers challenge"""

def get_a_down_arrow_of(n):
    pyramid = ""
    for i in range(n,0,-1):
        num_pattern = ""
        for j in range(1,i+1):
            num_pattern += str(j%10)
        pyramid += " "*(n-i) + num_pattern + num_pattern[-2::-1]+ "\n"
    return pyramid[:-1]