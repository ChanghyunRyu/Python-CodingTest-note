T = 10

for _ in range(1, T + 1):
    test_case = int(input())
    n = 100
    numbers = []
    result = -1
    for _ in range(n):
        numbers.append(list(map(int, input().split())))
    col_sum = [0]*n
    d1 = d2 = 0
    for i in range(n):
        result = max(result, sum(numbers[i]))
        d1 += numbers[i][i]
        d2 += numbers[n-1-i][i]
        for j in range(n):
            col_sum[j] += numbers[i][j]
    result = max(result, d1, d2, max(col_sum))
    print('#{} {}'.format(test_case, result))
