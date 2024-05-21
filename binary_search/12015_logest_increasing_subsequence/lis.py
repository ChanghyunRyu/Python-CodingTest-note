from bisect import bisect_left
INF = int(1e7)

n = int(input())
sequence = list(map(int, input().split()))
sub = [INF]
for s in sequence:
    if s > sub[len(sub)-1]:
        sub.append(s)
    else:
        index = bisect_left(sub, s)
        if sub[index] > s:
            sub[index] = s

print(len(sub))
