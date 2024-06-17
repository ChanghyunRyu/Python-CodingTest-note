from itertools import combinations


def solution(numbers):
    combination = combinations(numbers, 2)
    temp = set()
    for com in map(list, combination):
        num1 = com[0]
        num2 = com[1]
        temp.add(num1+num2)
    answer = list(temp)
    answer.sort()
    return answer


print(solution([2, 1, 3, 4, 1]))
