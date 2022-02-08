import time


# 큰 수의 법칙
# 시간제한: 1초, 메모리 제한: 128MB
# 시간제한이 1초인 경우
# O(n^3): n < 500, O(n^2): n < 2000, O(n*log(n)): n < 100000, O(n): n < 10000000

n, m, k = map(int, input().split(' '))
data = list(map(int, input().split(' ')))

data.sort(reverse=True)
first = data[0]
second = data[1]

result = (first*k+second)*(m//(k+1))+first*(m%(k+1))
print(result)
