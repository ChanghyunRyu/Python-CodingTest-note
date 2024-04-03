n = int(input())
nums = list(map(int, input().split()))

result = [0]*n
result[0] = nums[0]
for i in range(1, n):
    if result[i-1] < 0:
        result[i] = nums[i]
    else:
        result[i] = result[i-1] + nums[i]

print(max(result))
