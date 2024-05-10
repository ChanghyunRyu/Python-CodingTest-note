n = int(input())
adventurers = list(map(int, input().split()))
adventurers.sort()

result = 0

count = 0
for a in adventurers:
    count += 1
    if count >= a:
        result += 1
        count = 0
print(result)
