import sys
# 백준 기준 PyPy3로 제출 해야 시간 초과가 되지 않는다.


def minimal_print(color):
    prefix_sum = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 행과 열의 합이 짝수인 경우, 보드판 가장 왼쪽 위 색과 같은 색
            # 홀수인 경우 다른 색, 보드판 규칙과 같은 경우 0, 다른 경우 1을 기록
            if (i+j) % 2 == 0:
                # 해당 칸의 색은 보드의 가장 왼쪽 위와 같은 색 이어야 한다. 색이 다른 경우, 1
                value = chess[i-1][j-1] != color
            else:
                # 해당 칸의 색은 보드의 가장 왼쪽 위와 다른 색 이어야 한다. 즉, 보드 가장 왼쪽 위 색과 같은 경우 1
                value = chess[i-1][j-1] == color
            prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + value
    count = sys.maxsize
    # 누적합 2차원 배열 안에서 KxK 구간합 중 가장 작은 수를 찾아야 한다.
    for i in range(k, n+1):
        for j in range(k, m+1):
            value = prefix_sum[i][j] - prefix_sum[i-k][j] - prefix_sum[i][j-k] + prefix_sum[i-k][j-k]
            count = min(count, value)
    return count


n, m, k = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(sys.stdin.readline().strip())
print(min(minimal_print('B'), minimal_print('W')))
