from collections import defaultdict
result=defaultdict(int)
x=1000000
def zyklen(z):    
    kranke=1000
    tage=1
    while kranke<x:
        kranke*=2
        tage+=z
        result[tage]+=kranke
    return result
print(zyklen(3))
