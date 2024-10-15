## 여행 경로

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/43164

주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 
방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

### 제한 사항

- 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
- 주어진 공항 수는 3개 이상 10,000개 이하입니다.
- tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
- 주어진 항공권은 모두 사용해야 합니다.
- 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
- 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

---
### Problem Solved Check
- [x] 1회 24/08/02
- [x] 2회 24/10/15
- [ ] 3회

~~~
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
    
~~~
~~~
from collections import defaultdict
from collections import deque
from copy import deepcopy


def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    for g in graph:
        graph[g].sort()

    q = deque([('ICN', [], graph)])
    while q:
        now, result, g = q.popleft()
        result.append(now)
        if len(result) == len(tickets)+1:
            answer = result
            break

        next_cities = g[now]
        for i in range(len(next_cities)):
            new_arr = list(next_cities)
            new_graph = deepcopy(g)
            del new_arr[i]
            new_graph[now] = new_arr
            q.append((next_cities[i], list(result), new_graph))
    return answer
~~~