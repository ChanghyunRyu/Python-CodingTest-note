# 행렬을 사용한 fibonacci 수 구하기
# fibonacci 수 Fn = ([[1, 1], [1, 0]])^(n-1)의 1행 1열의 값
n = int(input())
mod = 1000000007


def mul_matrix(a, b):
    c = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            matrix_sum = 0
            for k in range(len(a[0])):
                matrix_sum = (matrix_sum+a[i][k]*b[k][j]) % mod
            c[i][j] = matrix_sum
    return c


def square_matrix(a, k):
    if k == 1 or k == 0:
        return a
    elif k == -1:
        return [[0]]
    else:
        square = square_matrix(a, k // 2)
        temp = mul_matrix(square, square)
        if k % 2 == 1.0:
            return mul_matrix(temp, a)
        else:
            return temp


rc = [[1, 1], [1, 0]]
result = square_matrix(rc, n-1)
print(result[0][0])
