def solution(n, target):
    dp = [set()]*9
    answer = -1
    for i in range(1, 9):
        dp[i] = fill_number(n, i, dp)
        if target in dp[i]:
            answer = i
            break
    return answer


def fill_number(number, index, dynamic):
    temp = set()
    temp.add(int(''.join([str(number)]*index)))
    if index == 1:
        return temp
    for i in range(1, index):
        num_group1 = dynamic[i]
        num_group2 = dynamic[index-i]
        for num1 in num_group1:
            for num2 in num_group2:
                temp.add(num1+num2)
                temp.add(num1-num2)
                if num2 != 0:
                    temp.add(num1//num2)
                temp.add(num1*num2)
    return temp


print(solution(5, 12))
print(solution(2, 11))
