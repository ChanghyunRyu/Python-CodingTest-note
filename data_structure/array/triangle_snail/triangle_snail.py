def solution(n):
    answer = []
    # n의 크기를 가진 삼각형 만들기 만들기
    triangle = [[0]*i for i in range(1, n+1)]
    dx = [0, 1, -1]
    dy = [1, 0, -1]

    # 현재 좌표, 카운트
    nx, ny = 0, 0
    cnt = 1
    end = n
    dx_idx, dy_idx = 0, 0
    for k in range(1, ((n**2+n)//2)+1):
        triangle[ny][nx] = k
        cnt += 1
        nx += dx[dx_idx]
        ny += dy[dy_idx]
        if cnt == end:
            cnt = 0
            end -= 1
            dx_idx = (dx_idx+1) % 3
            dy_idx = (dy_idx+1) % 3
    for tri in triangle:
        answer += tri
    return answer


print(solution(5))
