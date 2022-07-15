import math

t = int(input())
answer = []
for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    number = 0
    for j in range(n):
        cx, cy, cr = map(int, input().split())
        distance1 = math.sqrt((x1-cx)**2 + (y1-cy)**2)
        distance2 = math.sqrt((x2-cx)**2 + (y2-cy)**2)
        if distance1 < cr and distance2 < cr:
            continue
        if distance1 < cr or distance2 < cr:
            number += 1
    answer.append(number)

for ans in answer:
    print(ans)
