import re


def solution(s):
    pattern = '.(?=[0-9]{4,})'
    s = re.sub(pattern, '*', s)
    return s


print(solution('01033334444'))
print(solution('027778888'))
