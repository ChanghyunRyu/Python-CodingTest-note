from bisect import bisect_left


def solution(distance, rocks, n):
    rocks.sort()
    range_rocks = rocks[:bisect_left(rocks, distance)]
    range_rocks.append(distance)

    start = 0
    end = distance
    while start <= end:
        mid = (start+end)//2
        if chk_length(range_rocks, mid, n):
            answer = mid
            start = mid+1
        else:
            end = mid-1
    return answer


def chk_length(rocks, length, n):
    stack = [0]
    count = 0
    for r in rocks:
        now = r - stack[-1]
        if now < length:
            count += 1
            if count > n:
                return False
        else:
            stack.append(r)
    return True


print(solution(25, [2, 14, 11, 21, 17], 2))
