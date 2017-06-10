from functools import reduce
def is_palinrome(n):
    s1 = str(n)
    s2 = str(n)[::-1]#反转字符串
    return s1==s2

output = filter(is_palinrome,range(1,1000))
print(list(output))