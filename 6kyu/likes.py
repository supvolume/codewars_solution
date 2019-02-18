""" solution for Who likes it? challenge"""

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return names[0]+ " likes this"
    elif len(names) == 3:
        return ", ".join(names[0:2])+" and "+names[-1]+" like this"
    elif len(names) > 3:
        return ", ".join(names[0:2])+" and "+str(len(names)-2)+" others like this"
    else:
        return ", ".join(names[0:-1])+" and "+names[-1]+" like this"