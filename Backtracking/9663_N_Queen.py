# pypy3으로 제출했을 때만 정답
# 세로, 대각선+, 대각선- 를 각각 만들는 부분을 빠르게 생각하지 못 함. => 시간초과
n = int(input())
count = 0
length = set()
diagonal_minus = set()
diagonal_plus = set()


def nandqueen(x: int, y: int):
    global count
    if y in length or (x+y) in diagonal_minus or (x-y+n-1) in diagonal_plus:
        return
    else:
        if x == n-1:
            count += 1
            return
        length.add(y)
        diagonal_minus.add(x+y)
        diagonal_plus.add(x-y+n-1)
        for i in range(n):
            nandqueen(x+1, i)
        length.remove(y)
        diagonal_minus.remove(x+y)
        diagonal_plus.remove(x-y+n-1)


for i in range(n):
    nandqueen(0, i)
print(count)
