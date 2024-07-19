def solution(n):
    # 배열 생성
    arr = [[0]*(i+1) for i in range(n)]

    dx = [0, 1, -1]
    dy = [1, 0, -1]
    x = 0
    y = -1
    dx_idx = dy_idx = 0
    mark_num = 0
    for i in range(n, 0, -1):
        for j in range(i):
            mark_num += 1
            x += dx[dx_idx]
            y += dy[dy_idx]
            arr[y][x] = mark_num
        dx_idx = (dx_idx+1) % 3
        dy_idx = (dy_idx+1) % 3
    answer = []
    for line in arr:
        for num in line:
            answer.append(num)
    return answer


print(solution(4))
