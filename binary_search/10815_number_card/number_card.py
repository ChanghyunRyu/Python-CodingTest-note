n = int(input())
arr = list(map(int, input().split()))
num_arr = [0]*20000001
for a in arr:
    num_arr[a+10000000] += 1

m = int(input())
arr = list(map(int, input().split()))
for a in arr:
    print(num_arr[a+10000000], end=' ')
