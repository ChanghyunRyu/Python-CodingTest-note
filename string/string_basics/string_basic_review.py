import re


def solution(s):
    if (len(s) == 4 or len(s) == 6) and re.match('^[0-9]+$', s):
        return True
    return False


print(solution('a234'))
print(solution('12a3'))
print(solution('1234'))

