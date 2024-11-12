dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(result, x, y, k, is_used, route):
    flag = False
    route.append((x, y))
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        check = 0 <= nx < n and 0 <= ny < n and (nx, ny) not in route
        if check and arr[x][y] > arr[nx][ny]:
            flag = True
            dfs(result, nx, ny, k, is_used, list(route))
        if check and not is_used:
            for j in range(1, k+1):
                if arr[x][y] > (arr[nx][ny]-j):
                    arr[nx][ny] -= j
                    dfs(result, nx, ny, k, True, list(route))
                    arr[nx][ny] += j
    if not flag:
        result.append(len(route))


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    max_h = 0
    for i in range(n):
        for j in range(n):
            if max_h < arr[i][j]:
                max_h = arr[i][j]
                max_arr = [(i, j)]
            elif max_h == arr[i][j]:
                max_arr.append((i, j))
    result = []
    for x, y in max_arr:
        dfs(result, x, y, k, False, [])
    answer = max(result)
    print('#{} {}'.format(test_case, answer))
