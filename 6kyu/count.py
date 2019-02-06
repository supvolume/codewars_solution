"""solution for Count characters in your string challenge
count all character in string and return dictionary"""

def count(string):
    count={}
    for cha in string:
        count.setdefault(cha,0)
        count[cha]=count[cha]+1
    return count
