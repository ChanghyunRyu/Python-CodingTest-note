import sys


def getRect(h):
    # n = 주어진 사각형 개수
    n = len(h)
    if n == 1:
        return h[0]
    # 주어진 히스토그램을 반으로 나눠 왼쪽에서 가장 큰 직사각형(left_r), 오른쪽에서 가장 큰 직사각형(right_r)으로 정의
    mid = n // 2
    left_r = getRect(h[:mid])
    right_r = getRect(h[mid:])
    # 두 영역이 합쳐질 때 생기는 직사각형 검사
    l = mid-1
    r = mid
    under_w = 2
    min_h = min(h[l], h[r])
    max_area = under_w * min_h

    while 0 <= l and r+1 <= n:
        lh = h[l-1] if l > 0 else 0
        rh = h[r+1] if r < n-1 else 0
        min_h = min(min_h, lh) if lh > rh else min(min_h, rh)
        if lh > rh:
            l -= 1
        else:
            r += 1
        under_w += 1
        max_area = max(max_area, under_w * min_h)

    return max(left_r, right_r, max_area)


question = []
while True:
    heights = list(map(int, sys.stdin.readline().split()))
    if len(heights) == 1 and heights[0] == 0:
        break
    question.append(heights)
for q in question:
    print(getRect(q[1:]))
