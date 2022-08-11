n = int(input())
m = int(input())
graph = [[] for j in range(n)]
for i in range(m):
    com1, com2 = map(int, input().split())
    graph[com1-1].append(com2)
    graph[com2-1].append(com1)

visited_b = [False for i in range(n)]


def virus_dfs(graph, v, visit):
    if not visit[v-1]:
        visit[v-1] = True
        nodes = graph[v-1]
        for node in nodes:
            virus_dfs(graph, node, visit)


count = 0
virus_dfs(graph, 1, visited_b)
for i in range(1,n):
    if visited_b[i]:
        count += 1
print(count)
