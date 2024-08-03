from functools import cmp_to_key


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=cmp_to_key(compare), reverse=True)
    if numbers[0] == '0':
        return '0'
    return ''.join(numbers)


def compare(item1, item2):
    if int(item1+item2) > int(item2+item1):
        return 1
    elif int(item1+item2) < int(item2+item1):
        return -1
    else:
        return 0


print(solution([3, 30, 34, 5, 9]))
