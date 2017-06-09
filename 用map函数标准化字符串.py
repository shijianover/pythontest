from functools import reduce
L1=['adam','LISA','BARt']
def normalize(name):
    return name[0].upper()+name[1:].lower()

L2 = list(map(normalize,L1))
print(L2)