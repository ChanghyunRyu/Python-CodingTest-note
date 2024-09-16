def solution(board, skill):
    answer = 0
    prefix_sum = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for i in range(len(skill)):
        correction_skill(prefix_sum, skill[i])

    for i in range(len(prefix_sum)-1):
        for j in range(len(prefix_sum[0])-1):
            prefix_sum[i][j+1] += prefix_sum[i][j]
    for j in range(len(prefix_sum[0])-1):
        for i in range(len(prefix_sum)-1):
            prefix_sum[i+1][j] += prefix_sum[i][j]
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += prefix_sum[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer


def correction_skill(board, skill):
    t, x1, y1, x2, y2, degree = skill
    if t == 1:
        degree *= -1
    board[x1][y1] += degree
    board[x1][y2+1] += -degree
    board[x2+1][y1] += -degree
    board[x2+1][y2+1] += degree


board_temp = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill_temp = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
print(solution(board_temp, skill_temp))
