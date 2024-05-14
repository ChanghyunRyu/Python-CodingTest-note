t = int(input())
btn = [300, 60, 10]
result = []
for i in range(3):
    result.append(t // btn[i])
    t %= btn[i]
if t == 0:
    for r in result:
        print(r, end=' ')
else:
    print(-1)
