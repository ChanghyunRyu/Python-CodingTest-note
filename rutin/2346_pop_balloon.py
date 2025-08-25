n = int(input())
nums = list(enumerate(map(int, input().split()), start=1))

result = []
index = 0

while len(nums) > 1:
    now, num = nums[index]
    nums.remove(nums[index])
    result.append(now)
    # index 수정
    if num > 0:
        num -= 1
    index = (index+num) % len(nums)
else:
    result.append(nums[0][0])

for r in result:
    print(r, end=' ')
