n, k = map(int, input().split())

answer = 0
count = 0
for i in range(1, n+1):
    if n % i == 0:
        print(i)
        count += 1
    if count == k:
        answer = i
        break
print(answer)
