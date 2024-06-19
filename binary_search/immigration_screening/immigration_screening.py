def solution(n, times):
    start = 1
    end = min(times)*n
    while start <= end:
        mid = (start+end)//2
        if check_time(mid, times, n):
            answer = mid
            end = mid-1
        else:
            start = mid+1
    return answer


def check_time(chk_time, times, people):
    temp = 0
    for time in times:
        temp += chk_time//time
    if temp >= people:
        return True
    else:
        return False


print(solution(6, [7, 10]))
