n, k = map(int, input().split())
nums = [i+1 for i in range(n)]
result = []
target = k
while len(nums) > 0:
    target = target % len(nums)
    if target == 0:
        target = len(nums)
    result.append(nums[target-1])
    del nums[target-1]
    target += k - 1
print('<', end='')
for i in range(len(result)):
    if i == len(result)-1:
        print(result[i], end='')
    else:
        print(result[i], end=', ')
print('>')
