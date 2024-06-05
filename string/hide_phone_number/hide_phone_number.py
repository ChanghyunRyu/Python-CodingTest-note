import re


def solution(phone_number):
    return re.sub('\d(?=\d{4})', '*', phone_number)


print(solution("01033334444"))