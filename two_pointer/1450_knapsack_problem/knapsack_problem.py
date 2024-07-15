from itertools import combinations
from bisect import bisect_right

n, c = map(int, input().split())
items = list(map(int, input().split()))
index = n//2

a = items[:index]
b = items[index:]
a_list = [0]
b_list = [0]
for i in range(1, len(a)+1):
    for com in combinations(a, i):
        a_list.append(sum(com))

for i in range(1, len(b)+1):
    for com in combinations(b, i):
        b_list.append(sum(com))
b_list.sort()
count = 0

for i in a_list:
    count += bisect_right(b_list, c-i)
print(count)
