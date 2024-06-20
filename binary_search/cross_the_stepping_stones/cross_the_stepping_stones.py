def solution(stones, k):
    start = 1
    end = max(stones)
    while start <= end:
        mid = (start+end)//2
        if chk_cross_stones(stones, k, mid):
            answer = mid
            start = mid+1
        else:
            end = mid-1
    return answer


def chk_cross_stones(stones, k, check):
    count = 0
    for s in stones:
        if s-check < 0:
            count += 1
            if count >= k:
                return False
        else:
            count = 0
    return True


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
