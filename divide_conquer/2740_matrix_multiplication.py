import sys

n, m = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

B = []
m, k = map(int, input().split())
for i in range(m):
    B.append(list(map(int, sys.stdin.readline().split())))

# 곱셈 진행
c = [[0]*k for i in range(n)]
for i in range(n):
    for j in range(k):
        matrix_mul = 0
        for t in range(m):
            matrix_mul += A[i][t]*B[t][j]
        c[i][j] = matrix_mul
for row in c:
    for col in row:
        print(col, end=' ')
    print()

