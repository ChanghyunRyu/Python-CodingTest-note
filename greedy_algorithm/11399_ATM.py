# 백준 11399번 문제 ATM
n = int(input())
times = list(map(int, input().split()))

times.sort()
result = 0
for time in times:
    result += time*n
    n -= 1
print(result)
