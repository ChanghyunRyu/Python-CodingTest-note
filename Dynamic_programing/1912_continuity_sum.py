n = int(input())
nums = list(map(int, input().split()))
result = temp = nums[0]
for i in range(1, len(nums)):
    temp += nums[i]
    if nums[i] > temp:
        temp = nums[i]
    if temp > result:
        result = temp
print(result)
