# 초반 재귀함수 디자인 당시, 너무 생각이 많았음 + 디자인이 끔찍했음.
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def find_ice(x, y):
    if x >= m or y >= n:
        return False
    if graph[y][x] == 1:
        return False
    elif graph[y][x] == 0:
        graph[y][x] = 1
        find_ice(x, y+1)
        find_ice(x+1, y)
        return True


result = 0
for i in range(n):
    for j in range(m):
        if find_ice(j, i):
            print("{} {}".format(i, j))
            result += 1
print(result)
