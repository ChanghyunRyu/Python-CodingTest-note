import sys
sys.setrecursionlimit(10000)


N, L, R = map(int, input().split())
countries = []
for _ in range(N):
    countries.append(list(map(int, sys.stdin.readline().split())))


# (x, y): 좌표, visited: 방문 여부, country: 나라 배열 (l, r): 범위, s: 나라 집합
def dfs(x, y, visited, country, l, r, s):
    if visited[x][y]:
        return
    else:
        visited[x][y] = True
        s.add((x, y))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        check = 0 <= nx < len(visited) and 0 <= ny < len(visited)
        if check and l <= abs(country[x][y]-country[nx][ny]) <= r:
            dfs(nx, ny, visited, country, l, r, s)


flag = True
count = 0
while flag:
    v = [[False]*N for _ in range(N)]
    flag = False
    federations = []
    for i in range(N):
        for j in range(N):
            new_federation = set()
            dfs(i, j, v, countries, L, R, new_federation)
            if len(new_federation) > 1:
                federations.append(new_federation)

    if len(federations) == 0:
        continue
    count += 1
    flag = True
    for federation in federations:
        population = 0
        for r, c in federation:
            population += countries[r][c]
        for r, c in federation:
            countries[r][c] = (population//len(federation))
print(count)
