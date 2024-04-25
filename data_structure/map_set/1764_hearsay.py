# 첫번째 실패: 시간초과
# 문자열이다보니 이진탐색을 적용한다는 것을 처음에 생각하지 못했다.
# 개인적인 추가) in을 사용하는 것은 시간적인 시점에서 보면 굉장히 손해를 많이 보는 방법으로 보인다.
import sys

n, m = map(int, input().split())
cant_see = []
cant_listen = []
for i in range(n):
    cant_see.append(sys.stdin.readline())
for j in range(m):
    cant_listen.append(sys.stdin.readline())
cant_see.sort()
cant_listen.sort()


def check_person(target, start, end):
    if start > end:
        return False
    else:
        mid = (start+end)//2
        if cant_listen[mid] == target:
            return True
        elif cant_listen[mid] > target:
            return check_person(target, start, mid-1)
        else:
            return check_person(target, mid+1, end)


hearsay = []
for person in cant_see:
    if check_person(person, 0, len(cant_listen)-1):
        hearsay.append(person)

print(len(hearsay))
for person in hearsay:
    print(person, end='')
