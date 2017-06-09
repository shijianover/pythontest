from functools import reduce
L =[1,3,65,654,43,65]
def add(x,y):
    return x+y
print(reduce(add,L))