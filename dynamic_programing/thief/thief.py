def solution(money):
    dp_start_one = [0]*(len(money)-1)
    dp_start_one[0] = dp_start_one[1] = money[0]
    for i in range(2, len(money)-1):
        dp_start_one[i] = max(dp_start_one[i-1], dp_start_one[i-2]+money[i])

    dp_start_two = [0]*len(money)
    dp_start_two[0] = 0
    dp_start_two[1] = money[1]
    for i in range(2, len(money)):
        dp_start_two[i] = max(dp_start_two[i-1], dp_start_two[i-2]+money[i])

    return max(dp_start_one[-1], dp_start_two[-1])


print(solution([1, 2, 3, 1]))
print(solution([10, 5, 3, 1, 10]))
