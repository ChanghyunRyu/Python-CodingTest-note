# 첫 번째 실패: 시간초과
# in을 사용하기에는 시간이 너무 많이 소모된다.
# 체크에 이진탐색을 사용 = 입력 정수의 경우의 수를 살펴서 예상 시간에 대해 잘 대처해야한다.
n = int(input())
cards = list(map(int, input().split()))
cards = sorted(cards)
m = int(input())
checks = list(map(int, input().split()))


def check_number(number, start, end):
    if start > end:
        return False
    else:
        mid = (start+end)//2
        if cards[mid] == number:
            return True
        elif cards[mid] > number:
            return check_number(number, start, mid-1)
        else:
            return check_number(number, mid+1, end)


answer = ''
for check in checks:
    if check_number(check, 0, len(cards)-1):
        answer += '1 '
    else:
        answer += '0 '
print(answer)
