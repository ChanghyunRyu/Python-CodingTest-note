import math

n = int(input())
answer = []
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            answer.append(-1)
        else:
            answer.append(0)
        continue
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance == r1+r2 or distance == abs(r1-r2):
        answer.append(1)
    elif abs(r1-r2) < distance < r1+r2:
        answer.append(2)
    else:
        answer.append(0)
for ans in answer:
    print(ans)
