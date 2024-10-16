def solution(citations):
    h_index = [0]*10001
    for citation in citations:
        h_index[citation] += 1
    for i in range(max(citations)-1, -1, -1):
        h_index[i] += h_index[i+1]
        if h_index[i+1] >= i+1:
            return i+1
    return 0


# print(solution([3, 0, 6, 1, 5]))
print(solution([0]))
