# 굉장히 특이한 문제: 시간제한은 무려 5초나 주지만 메모리 제한이 고작 8MB임
# 8MB: int[2000000] 정도 가능, 단 숫자는 10000까지 자연수
# 메모리 제한이 있고 들어갈 수 있는 숫자의 범위가 작다는 것에 주목 = 계수정렬
import sys

data = [0 for i in range(10000)]
n = int(input())
for i in range(n):
    index = int(sys.stdin.readline())-1
    data[index] += 1

for i in range(len(data)):
    for j in range(data[i]):
        print(i+1)
