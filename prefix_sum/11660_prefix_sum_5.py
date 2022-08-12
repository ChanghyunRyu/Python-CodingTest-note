# 아이디어를 떠오리는 것보다 누적합과 정답을 계산할 때, 중복으로 더하거나 뺀 부분을 생각해주는 것을 자주 까먹었다.
# 해당 부분을 신경쓰면서 누적합을 적용하면 크게 어려운 문제는 아니다.
import sys
n, m = map(int, input().split())
nums = [[0]*(n+1)]
for i in range(n):
    temp = [0]+list(map(int, sys.stdin.readline().split()))
    nums.append(temp)
q = []
for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    q.append((x1, y1, x2, y2))
prefix_sum = [[0]*(n+1) for i in range(n+1)]
for i in range(n):
    for j in range(n):
        prefix_sum[i+1][j+1] = prefix_sum[i+1][j] + prefix_sum[i][j+1] + nums[i+1][j+1] - prefix_sum[i][j]
for question in q:
    x1, y1, x2, y2 = question[0], question[1], question[2], question[3]
    answer = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
    print(answer)

