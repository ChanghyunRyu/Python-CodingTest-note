def solution(citations):
    count = [0]*(max(citations)+1)
    for i in citations:
        count[i] += 1
    answer = 0
    prefix = [0]*len(count)
    prefix[len(prefix)-1] = count[len(count)-1]
    for i in range(len(count)-2, -1, -1):
        prefix[i] = prefix[i+1]+count[i]
        if prefix[i] >= i:
            answer = max(i, answer)
    return answer


print(solution([3, 0, 6, 1, 5]))
print(solution([4, 0, 6, 6, 6]))
