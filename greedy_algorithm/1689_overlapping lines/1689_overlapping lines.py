import sys

points = []
n = int(input())
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    points.append((s, 1))
    points.append((e, -1))

points.sort()
result = 0
check = 0

for point in points:
    # 선이 시작 +1, 선이 끝나면 -1을 해준다.
    check += point[1]
    result = max(result, check)

print(result)
