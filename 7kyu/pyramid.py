""" solution for Return pyramids challenge
build a pyramid in a given hight"""

def pyramid(n):
    pyramid =  ""
    for i in range(1, n):
        pyramid += " "*(n-i) + "/"+ " "*((i-1)*2)+"\\\n"
    pyramid += "/" + "_"*(n*2-2)+"\\\n"
    return pyramid
