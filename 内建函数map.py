def add(x,y,f):
    return f(x)+f(y)

def abs(x):
    if x>0:
        return x
    if x<0:
        return -x
x = map(abs,[-1,3,4,-34])
for m in list(x):
    print(m)