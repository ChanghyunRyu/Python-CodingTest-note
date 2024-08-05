def solution(n, times):
    answer = 0
    start, end = 1, min(times)*n
    while start <= end:
        mid = (start+end)//2
        if check_times(mid, n, times):
            answer = mid
            end = mid-1
        else:
            start = mid+1
    return answer


def check_times(target, n, times):
    result = 0
    for time in times:
        result += target//time
    if result >= n:
        return True
    else:
        return False


print(solution(6, [7, 10]))
