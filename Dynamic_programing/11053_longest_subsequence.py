n = int(input())
sequence = [0] + list(map(int, input().split()))
counts = [0] * (len(sequence)+1)
for i in range(len(sequence)):
    if i == 0:
        continue
    temp = 0
    for j in range(i):
        if sequence[i] > sequence[i-j-1] and temp < counts[i-j-1]+1:
            temp = counts[i-j-1] + 1
    counts[i] = temp
print(max(counts))
