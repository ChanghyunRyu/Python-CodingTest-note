def solution(stones, k):
    answer = 0
    start, end = 1, max(stones)
    while start <= end:
        mid = (start+end)//2
        if check_step_stones(mid, stones, k):
            answer = mid
            start = mid+1
        else:
            end = mid-1
    return answer


def check_step_stones(target, stones, k):
    chance = k-1
    for stone in stones:
        if stone >= target:
            chance = k-1
            continue
        if chance > 0:
            chance -= 1
        else:
            return False
    return True


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
