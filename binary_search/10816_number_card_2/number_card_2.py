n = int(input())
card = list(map(int, input().split()))

m = int(input())
number = list(map(int, input().split()))

arr = [0]*20000001
for c in card:
    arr[c+10000000] += 1

for n in number:
    print(arr[n+10000000], end=' ')
