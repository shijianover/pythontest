from functools import reduce
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,}[s]
def fn(x,y):
    return x*10+y



def str2float(s):
    s1,s2=s.split('.')
    return reduce(fn,map(char2num,s1))+reduce(fn,map(char2num,s2))/pow(10,len(s2))


print(str2float("123.43"))



