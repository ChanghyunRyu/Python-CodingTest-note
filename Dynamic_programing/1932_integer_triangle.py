import sys

n = int(input())
result = [0]
for i in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    temp = []
    for index in range(len(nums)):
        if index == 0:
            temp.append(result[index] + nums[index])
        elif index == len(nums) - 1:
            temp.append(result[index - 1] + nums[index])
        else:
            temp.append(max(result[index] + nums[index], result[index - 1] + nums[index]))
    result = temp
result.sort(reverse=True)
print(result[0])
