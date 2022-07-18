# 자물쇠와 열쇠의 관계를 어떻게 표현할 것인가?
# 모든 케이스를 조사하는 백트래킹을 사용
exam_key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
exam_lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


# 어떻게 열쇠를 회전시킬 것인가?
# 회전된 열쇠의 좌표 (i, j) = 기존 열쇠의(n-1-j, i), n은 열쇠의 크기
def rotate(key):
    key_len = len(key)
    rotate_key = [[0] * key_len for i in range(key_len)]
    for i in range(key_len):
        for j in range(key_len):
            rotate_key[i][j] = key[key_len-1-j][i]
    return rotate_key


# 특정 좌표에서 시작하여 열쇠가 자물쇠에 맞는지 체크합니다.
def check_unlock(x, y, key, table):
    answer = True
    m = len(key)
    n = len(table)-(2*(m-1))
    # 테이블의 좌표 m x m 칸을 key 만큼 더해준다.
    # 열쇠와 자물쇠의 돌기가 부딪칠 경우 = 2
    # 열쇠가 자물쇠를 채워주지 못하는 경우 = 0
    for i in range(m):
        for j in range(m):
            table[x+i][y+j] += key[i][j]

    # 자물쇠를 푸는 조건에 맞는지 검사합니다.
    # 자물쇠 중 하나라도 1이 아닐 경우 = 0 or 2
    # 0 = 자물쇠의 빈 공간을 채우지 못 했으므로 False
    # 2 = 자물쇠와 열쇠의 돌기가 부딪혔으므로 False
    # 이처럼 두 배열의 조건을 확인할 때, 더하는 것으로 간단하게 표현할 수 있지 않은지 검토해보는 것이 중요하다. (자주 놓치는 부분)
    for i in range(n):
        for j in range(n):
            if table[m-1+i][m-1+j] != 1:
                answer = False

    # 더해주었던 열쇠만큼 다시 빼주는 작업입니다.
    for i in range(m):
        for j in range(m):
            table[x+i][y+j] -= key[i][j]
    return answer


def solution(key, lock):
    answer = False
    m = len(key)
    n = len(lock)
    # 열쇠를 하나하나 끼워넣을 테이블 생성 (열쇠는 자물쇠 밖으로 나갈수 있으므로 2*(m-1) + n 크기로 형성)
    solution_table = [[0] * (2*(m-1)+n) for i in range(2*(m-1)+n)]
    for i in range(n):
        for j in range(n):
            solution_table[i+m-1][j+m-1] = lock[i][j]

    # 각 좌표를 돌면서 열쇠를 회전시키면서 삽입 후 체크
    for x in range(m-1+n):
        for y in range(m-1+n):
            for i in range(4):
                key = rotate(key)
                if check_unlock(x, y, key, solution_table):
                    return True
    return answer


print(solution(exam_key, exam_lock))

