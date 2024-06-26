import sys
INF = int(1e6)

n = int(input())
marbles = []
min_x = min_y = INF
max_x = max_y = -INF
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y


print((max_x-min_x)*(max_y-min_y))
