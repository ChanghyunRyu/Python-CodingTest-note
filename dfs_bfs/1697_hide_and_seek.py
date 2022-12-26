# 백준 1697번 문제 숨박꼭질
# x2로 이동하거나 +-1로 이동이 가능
# 그리디처럼 풀면 최적해 안 나오는 경우의 수가 생김
from collections import deque

n, k = map(int, input().split())
graph = [0 for i in range(200000)]


def hide_and_seek(tagger, person):
    queue = deque([tagger])
    while queue:
        tag = queue.popleft()
        if tag == person:
            break
        choice = [tag+1, tag-1, tag*2]
        for ntag in choice:
            if ntag >= 200000 or ntag < 0:
                continue
            if graph[ntag] == 0 or graph[ntag] > graph[tag] + 1:
                graph[ntag] = graph[tag] + 1
                queue.append(ntag)


hide_and_seek(n, k)
print(graph[k])
