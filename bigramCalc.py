from collections import Counter

with open('example.txt') as f:
    data = f.read()

bigrams = Counter(data[i:i+2] for i in range(len(data)-1))
bigrams = sorted(((k, v) for k, v in bigrams.items()), key=lambda x:x[1])

print(bigrams)

doubles = [(k, v) for k, v in bigrams if k[0] == k[1]]

print(doubles)
