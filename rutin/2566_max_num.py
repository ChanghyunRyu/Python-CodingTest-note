nums = []
for _ in range(9):
    nums.append(list(map(int, input().split())))

result = -1
x = 0
y = 0
for i in range(9):
    for j in range(9):
        if nums[i][j] > result:
            result = nums[i][j]
            x = i
            y = j

print(result)
print('{} {}'.format(x+1, y+1))
