import sys

n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))

result = []
for i in range(n):
    result.append([0]*(i+1))
result[0][0] = tri[0][0]

for i in range(1, n):
    for j in range(len(result[i])):
        if j == 0: # 가장 왼쪽
            result[i][j] = result[i-1][j] + tri[i][j]
        elif j == len(result[i])-1: # 가장 오른쪽
            result[i][j] = result[i-1][j-1] + tri[i][j]
        else:
            result[i][j] = max(result[i-1][j], result[i-1][j-1]) + tri[i][j]

print(max(result[n-1]))
