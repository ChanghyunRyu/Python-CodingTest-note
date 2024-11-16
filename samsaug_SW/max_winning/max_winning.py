from itertools import combinations

T = int(input())


def dfs(depth, nums):
    if depth == change:
        return nums
    new_nums = set()
    for num in nums:
        for a, b in combinations(list(range(len(num))), 2):
            new_num = list(num)
            new_num[a], new_num[b] = new_num[b], new_num[a]
            new_nums.add(''.join(new_num))
    return dfs(depth + 1, new_nums)


for test_case in range(1, T + 1):
    number, change = input().split()

    change = int(change)
    numbers = set([number])
    r = dfs(0, numbers)
    answer = max(r)
    print('#{} {}'.format(test_case, answer))
