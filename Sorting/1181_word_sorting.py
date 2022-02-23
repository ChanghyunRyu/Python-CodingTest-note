n = int(input())
data = []
for i in range(n):
    data.append(input())

data = sorted(set(data), key=lambda x: (len(x), x))
for word in data:
    print(word)
