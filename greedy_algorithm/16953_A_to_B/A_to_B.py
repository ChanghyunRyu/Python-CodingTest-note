from collections import deque

a, b = map(int, input().split())
q = deque([(a, 1)])
result = -1
while q:
    num, count = q.popleft()
    if num == b:
        result = count
        break
    if num*2 <= b:
        q.append((num*2, count+1))
    if (num*10)+1 <= b:
        q.append(((num*10)+1, count+1))
print(result)
