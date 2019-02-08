""" solution for Abbreviate a Two Word Name challenge
return latter in the front of name and surname"""

def abbrevName(name):
    return (name.split()[0][0]+"."+name.split()[1][0]).upper()