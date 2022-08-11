n, k = map(int, input().split())
tems = list(map(int, input().split()))
result = 0
prefix = [0]
for tem in tems:
    result += tem
    prefix.append(result)

answer = -1e9
for i in range(n-k+1):
    answer = max(answer, prefix[i+k]-prefix[i])
print(answer)
