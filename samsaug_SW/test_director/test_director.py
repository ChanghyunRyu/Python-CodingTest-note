import math


n = int(input())
people = list(map(int, input().split()))
general, sub = map(int, input().split())

temp = 0
for i in range(n):
    temp += 1
    temp += math.ceil(max(0, people[i]-general)/sub)
print(temp)
