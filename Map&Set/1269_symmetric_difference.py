# 첫 번째 오류: 중복된 숫자가 들어갈거라는 생각을 하지 못 했다.
# => 질문을 보고 해당 부분을 파악 못 했다고 생각했는데, 애초에 "집합의 원소"를 입력받는다고 명시되기 때문에 중복이 없다고 생각이 된다.
# 해결 1: 굉장히 간단한 방법 = 파이썬에서는 집합간의 대칭 차집합을 ^ 연산을 통하여 구현할 수 있다.
# 간단한 해결법 제외 첫 번째 해결법이 적용되지 않는 이유는 무엇인가?
# A의 크기 - 교집합의 크기 + B의 크기 - 교집합의 크기
# 문제점: B 배열을 정렬하지 않고 이진탐색을 사용했다....
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()


def check_number(target, start, end):
    if start > end:
        return False
    else:
        mid = (start+end)//2
        if B[mid] == target:
            return True
        elif B[mid] > target:
            return check_number(target, start, mid-1)
        else:
            return check_number(target, mid+1, end)


intersection = set()
for a in A:
    if check_number(a, 0, len(B)-1):
        intersection.add(a)
print(len(A)-len(intersection)+len(B)-len(intersection))

# 두번째 코드
# n, m = map(int, input().split())
# A = set(map(int, input().split()))
# B = set(map(int, input().split()))
# print(A ^ B)
