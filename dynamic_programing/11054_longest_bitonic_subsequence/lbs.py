from bisect import bisect_left

n = int(input())
sequence = list(map(int, input().split()))
sequence_reverse = list(reversed(sequence))


def lis(arr):
    num = len(arr)
    dp = [0]*num
    dp[0] = 1
    subsequence = [arr[0]]
    for i in range(1, n):
        if subsequence[len(subsequence)-1] < arr[i]:
            subsequence.append(arr[i])
            dp[i] = len(subsequence)
        else:
            pos = bisect_left(subsequence, arr[i])
            dp[i] = pos+1
            if subsequence[pos] > arr[i]:
                subsequence[pos] = arr[i]
    return dp


dp_f = lis(sequence)
dp_r = lis(sequence_reverse)
result = 0
for i in range(n):
    result = max(result, dp_f[i]+dp_r[n-i-1]-1)
print(result)
