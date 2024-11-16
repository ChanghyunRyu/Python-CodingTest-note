for test_case in range(1, 11):
    N = int(input())
    b = list(map(int, input().split()))
    answer = 0
    for i in range(2, N-2):
        left = max(b[i-1], b[i-2])
        right = max(b[i+1], b[i+2])
        if left >= b[i] or right >= b[i]:
            continue
        answer += b[i] - max(left, right)
    print('#{} {}'.format(test_case, answer))
