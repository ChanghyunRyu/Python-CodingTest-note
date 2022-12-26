import math
# 이 문제를 무려 2번이나 틀렸음. 굉장히 간단하다고 생각했는데 실수만 2번 했다.
# 첫 번째 실수는 단순히 측을 계산할 때 나머지로 계산 한 것 딱 나눠 떨어지는 경우 최고층을 고려해야했음
# 두 번째 실수는 math.ceil()을 사용하는 데 바보같이 n//h를 사용한 것 몫에 올림을해도 소수점이 없는데 자주 하는 실수인 듯

t = int(input())
h_list = []
w_list = []
n_list = []
for i in range(t):
    h, w, n = map(int, list(input().split()))
    h_list.append(h)
    w_list.append(w)
    n_list.append(n)

for i in range(t):
    h = h_list[i]
    w = w_list[i]
    n = n_list[i]
    floor = n % h
    if floor == 0:
        floor = h
    number = math.ceil(n/h)
    print(floor, end='')
    print(format(number, '02'))
