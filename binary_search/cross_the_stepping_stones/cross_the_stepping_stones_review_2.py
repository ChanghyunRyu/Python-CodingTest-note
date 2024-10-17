def solution(stones, k):
    start, end = 1, max(stones)
    answer = start
    while start <= end:
        mid = (start+end)//2
        if check_step_stones(stones, mid, k):
            answer = mid
            start = mid+1
        else:
            end = mid-1
    return answer


def check_step_stones(stones, number, k):
    count = 0
    for stone in stones:
        step = stone - number
        if step >= 0:
            count = 0
        elif step < 0:
            count += 1
            if count >= k:
                return False
    return True


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
