def solution(n, times):
    start, end = 0, min(times)*n
    answer = end
    while start <= end:
        mid = (start+end)//2

        temp = 0
        for time in times:
            temp += mid//time
        if temp >= n:
            answer = mid
            end = mid-1
        else:
            start = mid+1
    return answer


print(solution(6, [7, 10]))
