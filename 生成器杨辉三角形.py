def trangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L=[L[i-1]+L[i]for i in range(len(L))]

n=0
t = trangles()
for m in t:
    print(m)
    n+=1
    if n==10:
        break
