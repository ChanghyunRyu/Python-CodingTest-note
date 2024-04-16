from collections import deque
INF = int(1e9)

n, k = map(int, input().split())
point = [INF] * 100001
point[n] = 0
q = deque([n])
result = 0
while q:
    node = q.popleft()
    if node == k:
        result = point[node]
        break

    if 0 <= node-1 and point[node-1] > point[node]+1:
        point[node-1] = point[node]+1
        q.append(node-1)
    if node*2 <= 100000 and point[node*2] > point[node]+1:
        point[node*2] = point[node]+1
        q.append(node*2)
    if node+1 <= 100000 and point[node+1] > point[node]+1:
        point[node+1] = point[node]+1
        q.append(node+1)

print(result)
