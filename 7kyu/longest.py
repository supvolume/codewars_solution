""" solution for Two to One challenge
sort distinct letters of s1+s2 """

def longest(s1, s2):
    return ''.join(sorted(list(dict.fromkeys(s1+s2))))
