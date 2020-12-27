from collections import Counter
import re
from math import log
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce

fname = 'crypto_christmas_2020.txt'

with open(fname) as f:
    data = f.read()

with open('example.txt', encoding='utf-8') as f:
    example = f.read()

def IC(data, alph=None):
    if not isinstance(data, Counter):
        data = Counter(data)
    if alph is None:
        alph = len(data)
    denom = sum(v for v in data.values())
    return sum(v*(v-1) for v in data.values())*alph/denom/(denom+1)


def dbIC(data, n):
    total = 0
    for i in range(n):
        total += IC(data[i::n], 26)
    return total / n

'''print('data:')       f
for d in range(1, 20):
        val = dbIC(data, d)
        print(f'd = {d}: {val}')

print('example:')
for d in range(1, 20):
        val = dbIC(example, d)
        print(f'd = {d}: {val}')
'''
def invmod(a, n):
    a, b = _gcd_inv(a, n)
    # at this point a is the gcd of the original inputs
    if a == 1:
        return b
    raise ValueError("Not invertible")

def _gcd_inv(a, n):
    b, c = 1, 0
    while n:
        q, r = divmod(a, n)
        a, b, c, n = n, c, b - q*c, r
    return a, b

def gcd(a, n):
    return _gcd_inv(a, n)[0]

def lcm(a, b):
    return a*b//gcd(a,b)

##example = ''.join(v.lower() for v in example if v.lower() in 'abcdefghijklmnopqrstuvwxyz')

ebigramsc = Counter(example[i:i+2] for i in range(len(example)-1))
ebigrams = sorted(((k, v) for k, v in ebigramsc.items()), key=lambda x:x[1])
logbigrams = {k:100*log(v) for k, v in ebigrams}

ectr = Counter(example)
ecommon = sorted(ectr.items(), key = lambda x:-x[1])
echarset = sorted(ectr)

def ICforD(data, d, charset):
    i = 0
    out = ''
    for c in data:
        out += charset[(charset.index(c)+i)%len(charset)]
        i += 1
        i %= d
    return IC(out, len(charset))

'''for d in range(1, 11):
    val = ICforD(example, d, echarset)
    print(f'd = {d:2}: {val}')'''

##ebigrams = [example[i:i+2] for i in range(len(example)-1)]
print(f'IC for example = {IC(ectr, 26)}')
##print(f'IC for example bigrams = {IC(Counter(ebigrams))}')


ctr = Counter(data)
nospace = list(set(ctr)-{' '})
charset = sorted(ctr)
print(f'IC = {IC(ctr, 26)}')

print(f'data is {len(data)} characters long.')

ecommonf = [(k, v) for k, v in ecommon if k in charset]


def kasiski(data, l):
    chunks = [data[i:i+l] for i in range(len(data)-l)]
    ctr = Counter(chunks)
    diffs = set()
    for k, v in ctr.items():
        if v > 1:
            ni = data.find(k)
            if ni == -1:
                break
            while True:
                nn = data.find(k, ni+l)
                if nn == -1:
                    break
                d = nn - ni
                diffs.add(d)
                ni = nn
    return diffs, reduce(lambda x,y:gcd(x,y), diffs)

##bigramsc = Counter((data[i], data[i+1]) for i in range(len(data)-1))
##bigrams = sorted(((k, v) for k, v in bigramsc.items()), key=lambda x:x[1])

##print(f'bigrams in data up to {len(significant)}')
##print(significant)
##
##es = ebigrams[-70:]
##print(f'ordinary bigrams up to {len(es)}')
##print(es)
##
##print('letter freq (data):')
##print(ctr)
##
##print('letter freq (english):')
##print(ectr)

n = 39

chunks = [data[i:i+n] for i in range(0, len(data), n)]

def splitchunk(chunk):
    return ' '.join(repr(chunk[i:i+13]) for i in range(0,n,13))

def dec(chunks, key):
    newchunks = []
    for chunk in chunks:
        newchunk = ''
        for c, tab in zip(chunk, key):
            try:
                newchunk += tab[c]
            except KeyError:
                newchunk += '?'
        newchunks.append(newchunk)
    return newchunks

def getpairs(data, d, i):
    for j in range(0, len(data)-i-2, d):
        yield data[j+i:j+i+2]

def getSig(data, d, i):
    pairs = Counter(getpairs(data, d, i))
    sigPairs = [(k, v) for k, v in pairs.items() if v > 9]
    return sorted(sigPairs, key=lambda x:-x[1])


pc = [Counter(getpairs(data, n, i)) for i in range(n)]

common =[sorted(Counter(data[i::n]).items(), key=lambda x:-x[1]) for i in range(n)]
common2 = [[k for k, v in entry] for entry in common]


'''key = [{} for i in range(n)]
key[4]['t'] = 'h'
key[34]['G'] = 'h'
key[37]['2'] = 'h'
key[2644%n]['p'] = 'o'
#key[33]['J'] = 'T'
#key[2]['h'] = '/'
#key[5]['h'] = '/'

cribs = [(0, '')]
for i, str in cribs:
    for j in range(len(str)):
        ij = i+j
        ki = ij%n
        key[ki][data[ij]] = str[j]

for i in range(n):
    key[i][common[i][0][0]] = ' '
    key[i][common[i][1][0]] = 'e'
    #if i == 33:
    #       key[i]['J'] = 't'
    #else:
    key[i][common[i][2][0]] = 't'
#       key[]'''

'''for i in range(n):
        key[i][common[i][0][0]] = '0'
        key[i][common[i][1][0]] = '1'
        key[i][common[i][2][0]] = '2'
        key[i][common[i][3][0]] = '3'
'''
##sigs = []
##
##for i in range(12):
##    sigs.append(getSig(data, 13, i))
##
##print(*sigs, sep='\n\n', end='\n\n')
##
##common = []
##for a, b in zip(sigs[1:], sigs[:-1]):
##    common.append(set(v[0][0] for v in a)&set(v[0][1] for v in b))
##
##print(*common, sep='\n\n', end='\n\n')

'''c = '/'
before = re.findall(f'(?:.|\\n)(?={c})', data)
after = re.findall(f'(?<={c})(?:.|\\n)', data)'''

#ctrn = [sorted((Counter(data[i::n]) for i in range(n)), key=lambda x:-x[1])]

kb = [sorted(Counter((data[i:i+2] for i in range(j,len(data)-1,n))).items(), key=lambda x:-x[1]) for j in range(n)]



'''max = 0
for d in range(1, 500):
        v = dbIC(data, d)
        if v > max:
                max = v
                dd = d

print(dd, max)
'''

##for chunk in chunks:
##    print(repr(chunk))

#dec(data, {'h':'e'})

##print(IC(ebigramsc, len(ebigramsc)))
##print(IC(bigramsc, len(bigramsc)))

def updatekey(candiatekey):
    global memo1, memo2
    for i in range(n):
        m1i = memo1[i]
        m2i = memo2[i]
        #memc = Counter(v for k, v in candidatekey[i])
        for j in range(1, len(candidatekey[i])):
            ptchar, oldkc = candidatekey[i][j]
            i1 = (i-1) % n
            i3 = (i+1) % n
            key1 = dict(candidatekey[i1])
            key3 = dict(candidatekey[i3])
            if ptchar not in m1i:
                m1i[ptchar] = [(a, v) for (a, b), v in kb[i1] if b == ptchar]
            if ptchar not in m2i:
                m2i[ptchar] = [(b, v) for (a, b), v in kb[i] if a == ptchar]
            m1c = [(key1[a], v) for a, v in m1i[ptchar]]
            m2c = [(key3[b], v) for b, v in m2i[ptchar]]
            oldCS = 0
            for a, v in m1c:
                try:
                    oldCS += logbigrams[a+oldkc]
                except KeyError:
                    pass
            for b, v in m2c:
                try:
                    oldCS += logbigrams[oldkc+b]
                except KeyError:
                    pass
            #targetScore = -sum(v-1 for k, v in memc.items())*100
            #memScore = targetScore
            #targetScore = 0
            #targetScore += sum(logbigrams[key1[a]+key2[b]]*v for (a, b), v in kb[i1] if key1[a]+key2[b] in logbigrams)
            #targetScore += sum(logbigrams[key2[a]+key3[b]]*v for (a, b), v in kb[i] if key2[a]+key3[b] in logbigrams)
            #print(targetScore)
            for char in nospace:
                newCS = 0
                for a, v in m1c:
                    try:
                        newCS += logbigrams[a+char]*v
                    except KeyError:
                        pass
                for b, v in m2c:
                    try:
                        newCS += logbigrams[char+b]*v
                    except KeyError:
                        pass
                if newCS > oldCS:
                    oldCS = newCS
                    #print(i, j, char)
                    candidatekey[i][j] = (ptchar, char)
                    changed = True
                    #memc = Counter(v for k, v in candidatekey[i])
                    #targetScore = -sum(v-1 for k, v in memc.items())*100

candidatekey = [[(j[0], k) for j, k in zip(common[i], (k for k, v in ecommon if k in common2[i]))] for i in range(n)]

#memo1 = [[None]*len(c) for c in candidatekey[i] for i in range(n)]
#memo2 = [[None]*len(c) for c in candidatekey[i] for i in range(n)]
memo1 = [{} for i in range(n)]
memo2 = [{} for i in range(n)]

updatekey(candidatekey)

import cProfile
cProfile.run('updatekey(candidatekey)')

changed = True
loops = 0
while changed:
    changed1 = False
    print(f'loop1: {loops}')
    updatekey(candidatekey)
    key = [dict(v) for v in candidatekey]
    loops += 1

    with open('decoded', 'w') as f:
        decoded = dec(chunks, key)
        for i in range(len(chunks)):
            j = i*n
            print(splitchunk(chunks[i]), file=f)
            print(splitchunk(decoded[i])+f'{j} {j+13} {j+26}', file=f)
            
print('finished')

GRAPHS = False

if GRAPHS:
    print('example')
    plt.figure()
    plt.bar([ord(v) for v in ectr.keys()], ectr.values())
    plt.show()

    for i in range(min(n, 5)):
        print(f'data[{i}::n]')

        kc = Counter(data[i::n])
        plt.figure()
        plt.bar([ord(v) for v in kc.keys()], kc.values())
        plt.show()

#print(list(len(set(data[i::n])) for i in range(n)))
