def solution(triangle):
    answer =[ [0]*i for i in range(1, len(triangle)+1)]
    answer[0][0] = triangle[0][0]
    for i in range(1, len(answer)):
        for j in range(len(answer[i])):
            left = right = 0
            if j-1 >= 0:
                left = answer[i-1][j-1]
            if j < len(answer[i-1]):
                right = answer[i-1][j]
            answer[i][j] = triangle[i][j] + max(left, right)
    return max(answer[len(answer)-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
