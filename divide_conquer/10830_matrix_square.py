import sys

n, B = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))


def mul_matrix(a, b):
    result = [[0]*n for _ in range(n)]
    for t in range(n):
        for s in range(n):
            matrix_mul = 0
            for r in range(n):
                matrix_mul += a[t][r]*b[r][s] % 1000
            result[t][s] = matrix_mul
    return result


def square_matrix(num):
    if num == 1:
        return A
    else:
        result = square_matrix(num//2)
        squareResult = mul_matrix(result, result)
        if num % 2 == 1:
            return mul_matrix(squareResult, A)
        else:
            return squareResult


A_B = square_matrix(B)
for i in range(n):
    for port in A_B[i]:
        print(port % 1000, end=' ')
    print()
