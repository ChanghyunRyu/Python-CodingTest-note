from functools import cmp_to_key


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(lambda x, y: int(x+y)-int(y+x)), reverse=True)
    answer = ''.join(numbers)
    if numbers[0] == '0':
        return '0'
    return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([110, 1]))
print(solution([555, 565, 566, 55, 56, 5, 54, 544, 549]))
print("5665656555555554954544")
