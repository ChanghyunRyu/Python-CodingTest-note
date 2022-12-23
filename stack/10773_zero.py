import sys

nums = []

k = int(input())
for i in range(k):
    num = int(sys.stdin.readline())
    if num != 0:
        nums.append(num)
    else:
        del nums[len(nums)-1]
print(sum(nums))
