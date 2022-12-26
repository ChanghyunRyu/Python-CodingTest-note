# 해당 문제가 최장 증가 수열을 구하는 문제라는 것을 파악하는 것이 중요했다.(눈치채지 못함)
# 전깃줄을 얼마나 뺄지를 생각하는 것이 아니라 얼마나 많이 남길지를 고민하는 문제!
import sys

n = int(input())
cords = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    cords.append((a, b))
cords.sort(key=lambda x: x[0])
counts = [1]*n
for i in range(1, len(cords)):
    max_temp = 1
    for j in range(i):
        if cords[i-j-1][1] < cords[i][1] and counts[i-j-1] + 1 > max_temp:
            max_temp = counts[i-j-1] + 1
    counts[i] = max_temp
print(n-max(counts))
