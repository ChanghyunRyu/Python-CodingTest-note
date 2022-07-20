import sys

n = int(input())
R = G = B = 0
for i in range(n):
    r, g, b = map(int, sys.stdin.readline().split())
    tempR, tempG, tempB = R, G, B
    R = min(tempG+r, tempB+r)
    G = min(tempR+g, tempB+g)
    B = min(tempR+b, tempG+b)
print(min(R, G, B))
