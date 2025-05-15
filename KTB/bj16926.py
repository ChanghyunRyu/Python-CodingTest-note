# N*M*R = 300*300*1000 = 90000000, 시간 초과
# 애초에 회전 = 주기

n, m, r = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 회전을 돌리는 세트는 더 작은 숫자의 //2 만큼
t = min(n, m)//2
for i in range(t):
    # 1차원 함수로 펴기
    x1, y1 = i, i
    x2, y2 = n-1-i, m-1-i

    layer = []
    for y in range(y1, y2):
        layer.append(arr[x1][y])
    for x in range(x1, x2):
        layer.append(arr[x][y2])
    for y in range(y2, y1, -1):
        layer.append(arr[x2][y])
    for x in range(x2, x1, -1):
        layer.append(arr[x][y1])

    tr = r % len(layer)
    rotated = layer[tr:] + layer[:tr]

    idx = 0
    for y in range(y1, y2):
        arr[x1][y] = rotated[idx]
        idx += 1
    for x in range(x1, x2):
        arr[x][y2] = rotated[idx]
        idx += 1
    for y in range(y2, y1, -1):
        arr[x2][y] = rotated[idx]
        idx += 1
    for x in range(x2, x1, -1):
        arr[x][y1] = rotated[idx]
        idx += 1

for row in arr:
    for num in row:
        print(num, end=" ")
    print()
