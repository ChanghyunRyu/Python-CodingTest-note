n, k = map(int, input().split())
data_a = list(map(int, input().split()))
data_b = list(map(int, input().split()))

data_a.sort()
data_b.sort(reverse=True)

for i in range(k):
    # 처음에 a의 원소가 b보다 큰 경우의 수를 생각하지 않아서 조건문을 넣지 않음. 예제에서는 맞았지만 전체 문제에서는 오답처리가 났을 것.
    if data_b[i] > data_a[i]:
        data_a[i], data_b[i] = data_b[i], data_a[i]
    else:
        break
sum = 0
for num in data_a:
    sum += num
print(sum)
