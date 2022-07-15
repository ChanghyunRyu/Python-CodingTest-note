import math
w, h, x, y, p = map(int, input().split())
r = h/2
number = 0
for i in range(p):
    x1, y1 = map(int, input().split())
    distance1 = math.sqrt((x-x1)**2 + ((y+r)-y1)**2)
    distance2 = math.sqrt(((x+w)-x1)**2 + ((y+r)-y1)**2)
    if distance2 <= r or distance1 <= r:
        number += 1
        continue
    if x <= x1 <= x+w and y <= y1 <= y+h:
        number += 1
print(number)
