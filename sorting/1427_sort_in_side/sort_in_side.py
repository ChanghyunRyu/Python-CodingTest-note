arr = input()
tmp = []
for i in arr:
    tmp.append(int(i))
tmp.sort(reverse=True)
for t in tmp:
    print(t, end='')
