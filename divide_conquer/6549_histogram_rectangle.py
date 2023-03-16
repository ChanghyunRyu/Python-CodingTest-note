import sys


def getRect(h):
    n = len(h)
    if n == 1:
        return h[0]
    mid = n // 2
    left_h = getRect(h[:mid])
    right_h = getRect(h[mid:])
    start = mid - 1
    end = mid
    under = 2
    min_h = min(h[start], h[end])
    max_size = under * min_h
    while start >= 0 and end <= n - 1:
        l = h[start - 1] if start > 0 else 0
        r = h[end + 1] if end < n - 1 else 0
        min_h = min(min_h, l) if l > r else min(min_h, r)
        if l > r:
            start -= 1
        else:
            end += 1
        under += 1
        max_size = max(max_size, under * min_h)
    return max(left_h, right_h, max_size)


question = []
while True:
    heights = list(map(int, sys.stdin.readline().split()))
    if len(heights) == 1 and heights[0] == 0:
        break
    question.append(heights)
for q in question:
    print(getRect(q[1:]))
