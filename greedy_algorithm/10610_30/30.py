nums = list(map(int, input()))
if sum(nums) % 3 == 0 and 0 in nums:
    nums.sort(reverse=True)
    for n in nums:
        print(n, end='')
else:
    print(-1)
