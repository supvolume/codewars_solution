""" solution for Calculating with Functions
return the calculated result"""

def zero(n=0):
    if type(n) == list:
        n.append(0)
        return int(operation(n))
    else:        
        return [n]
def one(n=1):
    if type(n) == list:
        n.append(1)
        return int(operation(n))
    else:        
        return [n]
def two(n=2):
    if type(n) == list:
        n.append(2)
        return int(operation(n))
    else:        
        return [n]
def three(n=3):
    if type(n) == list:
        n.append(3)
        return int(operation(n))
    else:        
        return [n]
def four(n=4):
    if type(n) == list:
        n.append(4)
        return int(operation(n))
    else:        
        return [n]
def five(n=5):
    if type(n) == list:
        n.append(5)
        return int(operation(n))
    else:        
        return [n]
def six(n=6):
    if type(n) == list:
        n.append(6)
        return int(operation(n))
    else:        
        return [n]
def seven(n=7):
    if type(n) == list:
        n.append(7)
        return int(operation(n))
    else:        
        return [n]
def eight(n=8):
    if type(n) == list:
        n.append(8)
        return int(operation(n))
    else:        
        return [n]
def nine(n=9):
    if type(n) == list:
        n.append(9)
        return int(operation(n))
    else:        
        return [n]

def plus(n):
    n.append("plus")
    return n
def minus(n):
    n.append("minus")
    return n
def times(n):
    n.append("times")
    return n
def divided_by(n):
    n.append("duvided")
    return n

def operation(n_list):
    if n_list[1] == "plus":
        return n_list[2] + n_list[0]
    elif n_list[1] == "minus":
        return n_list[2] - n_list[0]
    elif n_list[1] == "times":
        return n_list[2] * n_list[0]
    elif n_list[1] == "duvided":
        return n_list[2] / n_list[0]
