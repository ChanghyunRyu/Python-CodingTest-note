from copy import deepcopy


def solution(tickets):
    result = []
    graph = ticket_to_graph(tickets)
    stack = [('ICN', graph, [])]
    while stack:
        now, graph, answer = stack.pop()
        answer.append(now)
        if len(answer) == len(tickets)+1:
            result = answer
            break
        if now in graph and graph[now]:
            for i in range(len(graph[now])):
                new_graph = deepcopy(graph)
                next_node = new_graph[now].pop(i)
                stack.append((next_node, new_graph, list(answer)))
    return result


def ticket_to_graph(tickets):
    graph = {}
    for start, end in tickets:
        if start not in graph:
            graph[start] = [end]
        else:
            graph[start].append(end)
    for start in graph:
        graph[start].sort(reverse=True)
    return graph


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([["ICN", "AAA"], ["AAA", "ICN"], ["ICN", "CCC"], ["CCC", "ICN"], ["ICN", "DDD"], ["DDD", "AAA"]]))
print(solution([["ICN", "BBB"], ["BBB", "ICN"], ["ICN", "AAA"]]))
