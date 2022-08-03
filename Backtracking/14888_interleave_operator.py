#
n = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_value = -1e9
min_value = 1e9


def dfs_op(i, result, add, sub, mul, div):
    global max_value, min_value
    if i == n:
        max_value = max(result, max_value)
        min_value = min(result, min_value)
    else:
        if add > 0:
            dfs_op(i+1, result + nums[i], add-1, sub, mul, div)
        if sub > 0:
            dfs_op(i+1, result - nums[i], add, sub-1, mul, div)
        if mul > 0:
            dfs_op(i+1, result * nums[i], add, sub, mul-1, div)
        if div > 0:
            dfs_op(i+1, int(result / nums[i]), add, sub, mul, div-1)


dfs_op(1, nums[0], operator[0], operator[1], operator[2], operator[3])
print(max_value)
print(min_value)
