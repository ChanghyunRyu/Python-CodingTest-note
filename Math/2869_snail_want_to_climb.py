import math

a, b, v = map(int, input().split())
day = math.ceil(v/(a-b))
print(day)
