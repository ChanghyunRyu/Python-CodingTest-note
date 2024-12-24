## [카카오 기출 문제] 도넛과 막대 그래프

---

[문제] https://school.programmers.co.kr/learn/courses/30/lessons/258711

루트 노드를 찾는 부분에서 조금 해맸다.  

루트 노드 = 노드에서 나가는 간선이 2개 이상, 들어오는 간선은 존재 x인 노드  

루트 노드를 찾아낸 이후는 다른 노드를 방문하며 그래프를 하나씩 찾았다.
1. 루트 탐색 도중 나가는 간선 혹은 들어오는 간선 둘 중 하나가 없는 노드가 있다 = 막대 그래프
2. 나가는 간선이 2개, 들어오는 간선이 2개 이상(루트 노드에서 올 수 있으므로) = 8자 그래프
3. 그 외는 도넛 그래프

그래프의 수를 모두 샌 후, 제출하면 정답

~~~
from collections import defaultdict


def solution(edges):
    answer = [0]*4
    in_graph = defaultdict(list)
    out_graph = defaultdict(list)
    for a, b in edges:
        in_graph[b].append(a)
        out_graph[a].append(b)

    # root 찾기
    root = 0
    for node in out_graph:
        if node not in in_graph and len(out_graph[node]) >= 2:
            root = node
            break
    answer[0] = root

    v = {root}
    for node in in_graph:
        if node in v:
            continue
        shape = dfs(node, v, in_graph, out_graph)
        if shape == 'donut':
            answer[1] += 1
        elif shape == 'stick':
            answer[2] += 1
        elif shape == 'eight':
            answer[3] += 1
    return answer


def dfs(node, visited, in_graph, out_graph):
    s = [node]
    shape = 'donut'
    while s:
        now = s.pop()
        visited.add(now)
        check = now in in_graph and now in out_graph
        if check and len(in_graph[now]) >= 2 and len(out_graph[now]) == 2:
            shape = 'eight'
        if now not in in_graph or now not in out_graph:
            shape = 'stick'
        if now in in_graph:
            next_nodes = in_graph[now]
            for next_node in next_nodes:
                if next_node not in visited:
                    s.append(next_node)
        if now in out_graph:
            next_nodes = out_graph[now]
            for next_node in next_nodes:
                if next_node not in visited:
                    s.append(next_node)
    return shape
~~~