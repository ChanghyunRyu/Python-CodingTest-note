def solution(citations):
    answer = 0
    count = [0]*10001
    for citation in citations:
        count[citation] += 1
    sum_count = 0
    for i in range(len(count)-1, 0, -1):
        sum_count += count[i]
        if sum_count >= i:
            answer = i
            break
    return answer


print(solution([3, 0, 6, 1, 5]))
