### floyd_warsall_algorithm.py

노드의 개수가 N개일 때 알고리즘상으로 N번의 단계를 수행하며, 각 단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐가는 모든 경로를 고려한다.  

따라서 플로이드-워셜 알고리즘의 시간복잡도는 O(N^3)이다.

~~~
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용을 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("Impossible", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

~~~
