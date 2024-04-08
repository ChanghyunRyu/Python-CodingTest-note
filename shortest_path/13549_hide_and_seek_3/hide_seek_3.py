from collections import deque
INF = int(1e9)

n, k = map(int, input().split())
result = [INF for _ in range(100001)]
result[n] = 0
q = deque()
q.append(n)

while q:
    now = q.popleft()
    if now == k:
        break
    if 0 <= (now-1) < 100001 and result[now-1] == INF:
        result[now-1] = result[now]+1
        q.append(now-1)
    if 0 <= (now*2) < 100001 and result[now*2] > result[now] + 1:
        result[now*2] = result[now]
        q.appendleft(now*2)
    if 0 <= (now+1) < 100001 and result[now+1] > result[now]+1:
        result[now+1] = result[now]+1
        q.append(now+1)

print(result[k])
