a, b = input().split()
if len(a) > len(b):
    big = a
    small = b
else:
    big = b
    small = a
sub = len(big)-len(small)
temp = list(map(int, big))
for i in range(len(small)):
    temp[i+sub] += int(small[i])
temp = list(reversed(temp))
for i in range(len(temp)-1):
    if temp[i] >= 10:
        temp[i] -= 10
        temp[i+1] += 1
temp = list(reversed(temp))
for num in temp:
    print(num, end='')
