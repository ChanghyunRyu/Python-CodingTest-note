# 백준 문제 2148번
# 해당 문제에 오기가 생겨서 DFS로 풀어보겠다고 몇시간을 날림.
# 1. 최단거리를 못 찾는 경우 - 해결
# 2. 시간 초과
# 최단 문제는 BFS 사용하는게 정말로 맞는 판단이고 재귀함수를 최대한 줄이려는 노력을 해봐도 보통 시간 초과를 겪게 됨.
# n, m 숫자가 작을 경우에만 DFS로 푸는 게 가능할 것 같음.
# 일단 제한을 풀어서 돌려본 결과, 결과 자체는 맞게 출력함.
n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def maze_search(x, y, count):
    if not (x == 0 and y == 0):
        maze[x][y] = count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if maze[nx][ny] == 1 or maze[nx][ny] > maze[x][y]+1:
            maze_search(nx, ny, maze[x][y]+1)


maze_search(0, 0, 1)
print(maze[n-1][m-1])
for i in range(n):
    print()
    for j in range(m):
        print("%3d" % maze[i][j], end=' ')
print()
