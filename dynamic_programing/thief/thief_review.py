def solution(money):
    dp_start_one = money[0] + get_max_return(money[2:len(money)-1])
    dp_start_two = money[1] + get_max_return(money[3:])
    dp_start_three = money[2] + get_max_return(money[4:]+[money[0]])
    return max(dp_start_one, dp_start_two, dp_start_three)


def get_max_return(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr)
    dp = [0]*len(arr)
    dp[0] = arr[0]
    dp[1] = arr[1]
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-2]+arr[i], dp[i-1])
    return dp[-1]


print(solution([1, 2, 3, 1]))
print(solution([0, 0, 2, 1, 0, 0, 1]))
print(solution([10, 5, 3, 1, 10]))
