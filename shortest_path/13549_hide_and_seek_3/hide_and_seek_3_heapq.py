import heapq
INF = int(1e9)

n, k = map(int, input().split())
result = [INF]*100001
result[n] = 0
q = []
heapq.heappush(q, (0, n))

while q:
    cost, now = heapq.heappop(q)
    if now == k:
        break
    if 0 <= now-1 and result[now-1] > cost+1:
        result[now-1] = cost+1
        heapq.heappush(q, (cost+1, now-1))
    if now*2 < 100001 and result[2*now] > cost:
        result[now*2] = cost
        heapq.heappush(q, (cost, now*2))
    if now+1 < 100001 and result[now+1] > cost+1:
        result[now+1] = cost+1
        heapq.heappush(q, (cost+1, now+1))

print(result[k])
