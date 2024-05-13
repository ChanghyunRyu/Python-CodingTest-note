import sys

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(sys.stdin.readline().rstrip()))
ropes.sort()

result = 0
for i in range(n):
    result = max(result, ropes[i]*(n-i))
print(result)
