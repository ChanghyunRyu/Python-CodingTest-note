n, s = map(int, input().split())
nums = list(map(int, input().split()))

prefix_sum = [0]
temp_sum = 0
for num in nums:
    temp_sum += num
    prefix_sum.append(temp_sum)

answer = n+1
start, end = 0, 1
while end < len(prefix_sum):
    if prefix_sum[end]-prefix_sum[start] < s:
        end += 1
    else:
        if end-start < answer:
            answer = end-start
        start += 1

if answer == n+1:
    print(0)
else:
    print(answer)
