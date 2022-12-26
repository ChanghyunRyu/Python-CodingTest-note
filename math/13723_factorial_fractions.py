n = int(input())
# 방정식 풀이를 통해 구하는 방법 구하고 각 진행마다 소인수분해를 함.
factor_list = [0]*10000
if n == 1:
    answer = 1
else:
    for num in range(2, n+1):
        d = 2
        while d <= num:
            if num % d == 0:
                num = num/d
                factor_list[d-1] += 1
            else:
                d += 1
answer = 1
for factor in factor_list:
    if factor == 0:
        continue
    else:
        answer *= (factor*2) + 1
print(answer)
