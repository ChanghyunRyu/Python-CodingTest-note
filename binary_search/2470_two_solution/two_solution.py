INF = int(1e10)

n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

count = INF
result = []
for i in range(len(solutions)-1):
    start = i+1
    end = len(solutions)-1
    while start <= end:
        mid = (start+end)//2
        mix = solutions[i]+solutions[mid]
        if abs(mix) < count:
            count = abs(mix)
            result = [solutions[i], solutions[mid]]
        if mix > 0:
            end = mid-1
        else:
            start = mid+1
for r in result:
    print(r, end=' ')
