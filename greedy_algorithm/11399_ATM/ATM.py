import sys

n = int(input())
people = list(map(int, sys.stdin.readline().split()))

people.sort()
result = 0
for i in range(len(people)):
    result += people[i]*(n-i)
print(result)
