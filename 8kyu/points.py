""" solution for Total amount of points challenge
 sum football points from result"""

def points(games):
    count=0
    for i in games:
        if i[0]>i[2]:
            count+=3
        elif i[0]==i[2]:
            count+=1
    return count
