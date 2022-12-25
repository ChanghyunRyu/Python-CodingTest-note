import sys

case = int(input())
for c in range(case):
    n, m = map(int, sys.stdin.readline().split())
    prints = list(map(int, sys.stdin.readline().split()))
    count = 1
    index = 0
    result = [0]*n
    while count <= n:
        if prints[index] == max(prints):
            result[index] = count
            prints[index] = -1
            count += 1
            index = (index+1) % n
        else:
            index = (index+1) % n
    print(result[m])
