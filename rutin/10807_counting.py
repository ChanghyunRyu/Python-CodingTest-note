n = int(input())

nums = list(map(int, input().split()))
target = int(input())

result = 0
for num in nums:
    if target == num:
        result +=1

print(result)
