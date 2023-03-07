# 파라매트릭 서치(parametric search)?
# 1. 특정 조건을 만족 하는 최댓값/최솟값을 구하는 형식의 문제 여야 한다.
# 2. 최댓값을 구하는 문제의 경우, 어떤 값이 조건을 만족 하면 그 값보다 작은 값은 모두 조건을 만족 해야 한다.
# 틀렸던 부분: 아예 자르지 않는 랜선이 존재할 수 있다. 처음 탐색 범위를 가장 짧은 랜선의 길이로 설정했으나 이 경우 반례가 존재한다.
# 파이썬 함수 round는 0.5를 모두 반올림하지 않는다 짝수로 옮기게 된다 => math.ceil 함수 사용
import sys
import math

k, n = map(int, input().split())
cables = []
for i in range(k):
    cables.append(int(sys.stdin.readline()))
left, right = 1, max(cables)
while left != right:
    mid = math.ceil((left+right)/2)
    value = 0
    for c in cables:
        value += int(c/mid)
    if value >= n:
        answer = mid
        left = mid
    else:
        right = mid-1
print(left)

