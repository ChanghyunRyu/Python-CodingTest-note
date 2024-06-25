n, k = map(int, input().split())

answer = 0
count = 0
for i in range(1, (n//2)+1):
    if n % i == 0:
        count += 1
    if count == k:
        answer = i
        break
if count+1 == k:
    answer = n
print(answer)
