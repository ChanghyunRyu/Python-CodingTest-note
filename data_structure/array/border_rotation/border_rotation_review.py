def solution(rows, columns, queries):
    arr = [list(range(i*columns+1, (i+1)*columns+1)) for i in range(rows)]
    answer = []
    for q in queries:
        start = (q[0]-1, q[1]-1)
        end = (q[2]-1, q[3]-1)
        arr, result = rotate_arr(start, end, arr)
        answer.append(result)
    return answer


def rotate_arr(start, end, arr):
    before_num = arr[start[0]][start[1]]
    min_num = before_num
    # 상단 이동, start = (1, 1), end(4, 3)
    for i in range(start[1]+1, end[1]+1):
        before_num, arr[start[0]][i] = arr[start[0]][i], before_num
        min_num = min(min_num, before_num)
    # 우측 이동
    for i in range(start[0]+1, end[0]+1):
        before_num, arr[i][end[1]] = arr[i][end[1]], before_num
        min_num = min(min_num, before_num)
    # 하단 이동
    for i in range(end[1]-1, start[1]-1, -1):
        before_num, arr[end[0]][i] = arr[end[0]][i], before_num
        min_num = min(min_num, before_num)
    # 좌측 이동
    for i in range(end[0]-1, start[0]-1, -1):
        before_num, arr[i][start[1]] = arr[i][start[1]], before_num
        min_num = min(min_num, before_num)
    return arr, min_num


query = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
print(solution(6, 6, query))
query = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
print(solution(3, 3, query))
