def solution(n, results):
    graph = [[0]*n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 'self'
    for winner, loser in results:
        graph[winner-1][loser-1] = 'win'
        graph[loser-1][winner-1] = 'lose'
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 'win' and graph[k][j] == 'win':
                    graph[i][j] = 'win'
                if graph[i][k] == 'lose' and graph[k][j] == 'lose':
                    graph[i][j] = 'lose'
    answer = 0
    for g in graph:
        if 0 not in g:
            answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
