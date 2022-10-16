# Linear Regression of Y on X
def regressionLine(x, y):
    x2 = [i**2 for i in x]
    xy = [i*j for i,j in zip(x,y)]
    a = ((sum(x2)*sum(y))-(sum(x)*sum(xy)))/((len(x)*sum(x2))-(sum(x)**2))
    b = ((len(x)*sum(xy))-(sum(x)*sum(y)))/((len(x)*sum(x2))-(sum(x)**2))
    return (round(a,4),round(b,4))
