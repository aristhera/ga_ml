from collections import defaultdict
result=defaultdict(int)
x=1000000
kranke=1000
tage=1
def zyklen(z):    
    global kranke, tage
    while kranke<x:
        kranke*=2
        tage+=z
        result[tage]+=kranke
    return result
print(zyklen(3))
