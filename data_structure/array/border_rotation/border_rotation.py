def solution(rows, columns, queries):
    answer = []
    # 숫자로 된 배열 만들기
    arr = []
    for i in range(rows):
        arr.append(list(range(i*columns+1, (i+1)*columns+1)))
    # query 별로 회전 시키기
    for start_x, start_y, end_x, end_y in queries:
        now_x, now_y = start_x-1, start_y
        before_num = arr[now_x][now_y-1]
        min_num = before_num
        while True:
            # 저장한 기존 칸의 수와 새로운 index 의 수 교체
            before_num, arr[now_x][now_y] = arr[now_x][now_y], before_num
            min_num = min(min_num, before_num)
            if now_x == start_x-1 and now_y == start_y-1:
                break
            # 다음 칸으로 이동
            if now_x == start_x-1 and now_y < end_y-1:
                now_y += 1
            elif now_y == end_y-1 and now_x < end_x-1:
                now_x += 1
            elif now_x == end_x-1 and now_y > start_y-1:
                now_y -= 1
            elif now_y == start_y-1:
                now_x -= 1
        answer.append(min_num)
    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3 , [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
