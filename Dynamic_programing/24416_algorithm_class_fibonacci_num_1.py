# 코드1의 실행 횟수는 피보나치 수 자체다
n = int(input())
f = [0]*40
f[0] = f[1] = 1
count = 0
for i in range(2, n):
    count += 1
    f[i] = f[i-1] + f[i-2]

print("{} {}".format(f[n-1], count))
