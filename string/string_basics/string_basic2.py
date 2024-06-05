import re


def solution(s):
    if (len(s) == 4 or len(s) == 6) and re.match('^\d*$', s):
        return True
    return False
