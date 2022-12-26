import sys

n = int(input())
data = []
for i in range(n):
    # input()을 사용하지 않고 sys.stdin.readline()을 사용했다.
    # input()의 경우, 줄 넘김이 발생하여 입력 시 시간을 많이 잡아먹는 단점이 있으므로 이런 식으로 사용하는 것이 좋다.
    # 특히 구현은 간단하나 시간초과를 유발하는 문제의 경우, 필히 사용하는 것이 좋다.
    data.append(int(sys.stdin.readline()))

data.sort()
for num in data:
    print(num)
