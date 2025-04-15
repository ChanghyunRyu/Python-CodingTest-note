p_sum = [0]*1002

num = 1
count = 0
for i in range(1, 1002):
    p_sum[i] = p_sum[i-1]+num
    if count == num:
        num += 1
        count = 1
    else:
        count += 1

n, m = map(int, input().split())
print(p_sum[m+1]-p_sum[n])
