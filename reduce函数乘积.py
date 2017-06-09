from functools import reduce
def chengji(x,y):
    return x*y
def pord(L):
    return reduce(chengji,L)

print(pord([1,2,4,4]))