from collections import Counter

with open('example.txt') as f:
    data = f.read()

charset = sorted(set(data))

def f(data, d):
    i = 0
    newdata = ''
    for c in data:
        newdata += charset[(charset.index(c)+i)%len(charset)]
        i += 1
        if i == d:
            i = 0
    ctr = Counter(newdata)
    num = denom = 0
    for v in ctr.values():
        num += v*(v-1)
        denom += v
    return num / (denom * (denom - 1))

for i in range(2, 20):
    print(i, f(data, i))
    
        
        
