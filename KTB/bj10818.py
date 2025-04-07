n = int(input())
nums = list(map(int, input().split()))
nums.sort()

print('{} {}'.format(nums[0], nums[-1]))
