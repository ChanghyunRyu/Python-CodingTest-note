n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

now = price[0]
result = 0
for i in range(n-1):
    result += now*length[i]
    now = min(now, price[i+1])
print(result)
